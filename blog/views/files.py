from blog.models.files import Files
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..forms import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, initial={
            'user': request.user,
            'path': request.FILES['fil'].name,
        })
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(form.instance.get_absolute_url())
    else:
        form = UploadFileForm()
    return render(request, 'blog/files/upload.html', {'form': form})


def download_file(request, path):
    fil = get_object_or_404(Files, pk=path)
    response = HttpResponse(fil.fil, content_type=fil.get_content_type())
    response['Content-Disposition'] = 'inline; filename=' + fil.fil.name
    return response
