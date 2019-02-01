from blog.models.files import Files
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..forms import UploadFileForm


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


def download_file(request, pk, ext):
    fil = get_object_or_404(Files, pk=pk)
    if not fil.fil.name.endswith(ext):
        raise Http404()
    response = HttpResponse(fil.fil, content_type=fil.get_content_type())
    response['Content-Disposition'] = 'inline; filename=' + fil.fil.name
    return response
