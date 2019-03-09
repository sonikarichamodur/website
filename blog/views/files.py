from blog.models.files import Files
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from ..forms import UploadFileForm
from django.views.decorators.cache import cache_page
from django.urls import reverse
from ..forms import UploadFileForm, DeleteForm
from ..models import Files
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


class BasicUploadView(LoginRequiredMixin, View):
    def get(self, request):
        files_list = Files.objects
        if request.user.has_perm('files_gui_all_list'):
            files_list = files_list.order_by('-pub_date').all()
        elif request.user.has_perm('files_gui_own_list'):
            files_list = files_list.filter(user=request.user).order_by('-pub_date').all()
        else:
            files_list = []

        files = {}
        # FIXME: Add pagination
        for fil in files_list[:10]:
            files[fil.pk] = dict(
                obj=fil,
                can_update=request.user.has_perm('files_gui_all_update'),
                can_delete=request.user.has_perm('files_gui_all_delete'),
            )
            if fil.user == request.user:
                files[fil.pk]['can_update'] = files[fil.pk]['can_update'] or request.user.has_perm(
                    'files_gui_own_update')
                files[fil.pk]['can_delete'] = files[fil.pk]['can_delete'] or request.user.has_perm(
                    'files_gui_own_delete')

        can_create = request.user.has_perm('files_gui_own_create')
        return render(self.request, 'blog/files/index.html', {'files': files, 'can_create': can_create, })

    def post(self, request):
        files = {'fil': self.request.FILES['file']}

        post = dict(self.request.POST).copy()
        post['title'] = 'Bulk %s' % files['fil'].name

        form = UploadFileForm(post, files)
        if form.is_valid():
            form.instance.user = request.user
            file = form.save()
            data = {'is_valid': True, 'name': file.get_rel_url(), 'url': file.get_absolute_url()}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, initial={
            'user': request.user,
        })
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(form.instance.get_absolute_url())
    else:
        form = UploadFileForm()
    return render(request, 'blog/files/upload.html', {'form': form})


@cache_page(60 * 60 * 1)
def download_file(request, pk, ext):
    fil = get_object_or_404(Files, pk=pk)
    if not fil.fil.name.endswith(ext):
        raise Http404()
    response = HttpResponse(fil.fil, content_type=fil.get_content_type())
    response['Content-Disposition'] = 'inline; filename=' + fil.fil.name
    return response


@login_required
def delete_file(request, pk, ext):
    fil = get_object_or_404(Files, pk=pk)
    if not fil.fil.name.endswith(ext):
        raise Http404()
    # This is stupid verbose but super clear
    if fil.user == request.user:
        if request.user.has_perm('files_gui_own_delete') or request.user.has_perm('files_gui_all_delete'):
            # Owns file and has one or both required perms
            pass
        else:
            # Owns file but lacks any perms
            raise HttpResponseNotAllowed()
    else:
        if request.user.has_perm('files_gui_all_delete'):
            # Doesn't own file and has all delete perm
            pass
        else:
            # Doesn't own file and lacks all perms
            raise HttpResponseNotAllowed()
    if request.method == 'POST':
        form = DeleteForm(request.POST, request.FILES)
        if form.is_valid():
            fil.delete()
            return HttpResponseRedirect(reverse('blog:upload_file'))
    else:
        form = DeleteForm()
    return render(request, 'blog/files/delete.html', {'form': form, 'fil': fil})


@login_required
def update_file(request, pk, ext):
    fil = get_object_or_404(Files, pk=pk)
    if not fil.fil.name.endswith(ext):
        raise Http404()
    # This is stupid verbose but super clear
    if fil.user == request.user:
        if request.user.has_perm('files_gui_own_update') or request.user.has_perm('files_gui_all_update'):
            # Owns file and has one or both required perms
            pass
        else:
            # Owns file but lacks any perms
            raise HttpResponseNotAllowed()
    else:
        if request.user.has_perm('files_gui_all_update'):
            # Doesn't own file and has all delete perm
            pass
        else:
            # Doesn't own file and lacks all perms
            raise HttpResponseNotAllowed()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            fil.title = form.instance.title
            fil.fil = form.instance.fil
            fil.user = form.instance.user
            fil.pub_date = timezone.now()
            fil.save()
            return HttpResponseRedirect(fil.get_absolute_url())
    else:
        form = UploadFileForm()
    return render(request, 'blog/files/update.html', {'form': form})
