from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import Http404
from blog.models.comment import Comment
from blog.models.meeting import Meeting
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Q
from datetime import timedelta


class MeetingCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Meeting
    fields = ['end_time', ]
    template_name = 'blog/create_meeting.html'
    login_url = reverse_lazy('login')
    permission_required = "blog.meeting_gui_can_create"

    def form_valid(self, form):
        form.instance.user = self.request.user

        # if self.kwargs['end_time'] <= (timezone.now() + timedelta(minutes=25)):
        #     return HttpResponse("meeting end time is set incorrectly", status=500)

        ret = super().form_valid(form)

        if self.object.end_time <= (timezone.now() + timedelta(minutes=25)):
            return HttpResponse("meeting end time is set incorrectly", status=500)

        if Meeting.objects.filter(start_time__lte=timezone.now()).filter(
                Q(end_time__isnull=True) | Q(end_time__gte=timezone.now())).count() > 0:
            return HttpResponse("cannot create multiple meetings", status=500)

        return ret

    def get_success_url(self):
        return reverse('blog:signin', kwargs={'pk': self.object.pk})
