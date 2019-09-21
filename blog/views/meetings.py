from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import Http404
from blog.models.comment import Comment
from blog.models.meeting import Meeting
from django.contrib.auth.mixins import PermissionRequiredMixin


class MeetingCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Meeting
    fields = ['start_time', 'end_time']
    template_name = 'blog/create_meeting.html'
    login_url = reverse_lazy('login')
    permission_required = "blog.meeting_gui_can_create"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:signin', kwargs={'pk': self.kwargs['pk']})
