from blog.models.files import Files
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..forms import UploadFileForm
from django.views.decorators.cache import cache_page

from .forms import UploadFileForm
from .models import Files

@login_required
class BasicUploadView(View):
    def get(self, request):
        files_list = Files.objects.all()
        return render(self.request, 'blog/files/index.html', {'files': files_list})

    def post(self, request):
        form = UploadFileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            file = form.save()
            data = {'is_valid': True, 'name': file.fil.name, 'url': file.fil.url}
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

