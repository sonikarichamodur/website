from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from ..models.signin import Signin
from ..models.meeting import Meeting
from django.http import HttpResponse
from django.utils import timezone
from ..forms import PasswordForm


@permission_required("blog.meeting_gui_can_create")
def end_meeting(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)

    if request.method != 'POST':
        return HttpResponse('expected POST', status=400)

    if meeting.end_time < timezone.now():
        return HttpResponse('meeting already over', status=500)

    form = PasswordForm(request.POST)
    if form.is_valid():
        if not request.user.check_password(form.cleaned_data['passwd']):
            return HttpResponse('bad password', status=500)

        meeting.end_time = timezone.now()
        meeting.save()

        return redirect("/")
    else:
        return HttpResponse('bad password', status=500)
