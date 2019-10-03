from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import Http404
from blog.models.comment import Comment
from blog.models.signin import Signin
from blog.models.meeting import Meeting
from blog.models.member import Member
from django.contrib.auth.mixins import PermissionRequiredMixin


class MeetingSignin(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Signin
    fields = ['user']
    template_name = 'blog/signin.html'
    login_url = reverse_lazy('login')
    permission_required = "blog.meeting_gui_can_create"

    def form_valid(self, form):
        form.instance.meeting = Meeting.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:signin', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        ctx = super(MeetingSignin, self).get_context_data(**kwargs)
        ctx['signed_in'] = Signin.objects.filter(end_time__isnull=True, signin__any=True,
                                                 meeting=Meeting.objects.get(pk=self.kwargs['pk'])).all()
        return ctx
