from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import Http404
from blog.models.comment import Comment
from blog.models.signin import Signin
from blog.models.meeting import Meeting
from blog.models.member import Member
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import redirect


from django.contrib.auth.mixins import PermissionRequiredMixin


class MeetingSignin(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Signin
    fields = ['user']
    template_name = 'blog/signin.html'
    login_url = reverse_lazy('login')
    permission_required = "blog.meeting_gui_can_create"

    def form_valid(self, form):
        form.instance.meeting = Meeting.objects.get(pk=self.kwargs['pk'])

        if form.instance.meeting.start_time > timezone.now():
            return HttpResponse('meeting has not started', status=500)

        if form.instance.meeting.end_time < timezone.now():
            return HttpResponse('meeting has ended', status=500)

        if Signin.objects.filter(meeting=form.instance.meeting, user__id=self.kwargs['user']).count() > 0:
            return redirect("/meeting/%d/" % form.instance.meeting.id)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:signin', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        ctx = super(MeetingSignin, self).get_context_data(**kwargs)
        ctx['signed_in'] = Signin.objects.filter(end_time__isnull=True,
                                                 meeting=Meeting.objects.get(pk=self.kwargs['pk'])).all()
        return ctx
