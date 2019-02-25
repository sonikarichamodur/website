from blog.models.files import Files
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from ..forms import UploadFileForm
from django.views.decorators.cache import cache_page
from django.urls import reverse
from ..forms import UploadFileForm
from ..models import Files
from django.contrib.auth.mixins import LoginRequiredMixin


class BasicUploadView(LoginRequiredMixin, View):
    def get(self, request):
        files_list = Files.objects.all()
        return render(self.request, 'blog/files/index.html', {'files': files_list})

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
