from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import forms
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from ..models.member import Member
from django.shortcuts import Http404, render
from blog.models.comment import Comment
from blog.models.meeting import Meeting, MeetingType
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from datetime import timedelta
from django.http import Http404
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from ..models.team import Team


class SigninForm(forms.Form):
    teams = MultipleChoiceField(
        choices=Team.objects.all().order_by('name').values_list("name", "display_name"),
        widget=CheckboxSelectMultiple,
    )


@permission_required("blog.meeting_gui_can_create")
def meeting(request):
    form = SigninForm(request.POST)

    if form.is_valid():
        m = Meeting(user=request.user)
        m.save()
        for choice in form.cleaned_data['teams']:
            ch = MeetingType(meeting=m, team=Team.objects.get(name=choice))
            ch.save()
        return HttpResponseRedirect(reverse('blog:signin', kwargs={'pk': m.pk}))

    return render(request, 'blog/create_meeting.html', {"form": form})
