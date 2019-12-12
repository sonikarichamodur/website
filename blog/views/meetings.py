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


class SigninForm(forms.Form):
    choices = MultipleChoiceField(choices=Member.TEAM, widget=CheckboxSelectMultiple)


@permission_required("blog.meeting_gui_can_create")
def meeting(request):
    form = SigninForm(request.POST)

    if form.is_valid():
        m = Meeting(user=request.user)
        m.save()
        for choice in form.cleaned_data['choices']:
            ch = MeetingType(meeting=m.id, subteam=choice)
            ch.save()
            return HttpResponseRedirect(reverse('blog:signin', kwargs={'pk': m.pk}))

    return render(request, 'blog/create_meeting.html', {"form": form})


class MeetingCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Meeting
    fields = []
    template_name = 'blog/create_meeting.html'
    login_url = reverse_lazy('login')
    permission_required = "blog.meeting_gui_can_create"

    def form_valid(self, form):
        form.instance.user = self.request.user

        # if self.kwargs['end_time'] <= (timezone.now() + timedelta(minutes=25)):
        #     return HttpResponse("meeting end time is set incorrectly", status=500)

        ret = super().form_valid(form)
        #
        # if self.object.end_time <= (timezone.now() + timedelta(minutes=25)):
        #     return HttpResponse("meeting end time is set incorrectly", status=500)

        # if Meeting.objects.filter(start_time__lte=timezone.now()).filter(
        #         Q(end_time__isnull=True) | Q(end_time__gte=timezone.now())).count() > 0:
        #     raise forms.ValidationError("cannot create multiple meetings")

        return ret

    def get_success_url(self):
        return reverse('blog:signin', kwargs={'pk': self.object.pk})
