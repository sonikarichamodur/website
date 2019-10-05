from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from ..models.signin import Signin
from ..models.meeting import Meeting
from django.http import HttpResponse
from django.utils import timezone


@permission_required("blog.meeting_gui_can_create")
def meetingSignOut(request, signId):
    user_signin = get_object_or_404(Signin, pk=signId)
    if user_signin.end_time is not None:
        return HttpResponse(status=500)

    if user_signin.meeting.end_time is not None:
        return HttpResponse(status=500)

    user_signin.end_time = timezone.now()
    user_signin.save()

    return redirect("/meeting/%d/" % user_signin.meeting.id)
