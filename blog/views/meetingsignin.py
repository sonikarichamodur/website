from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import Http404

from blog.forms import PasswordForm
from blog.models.comment import Comment
from blog.models.signin import Signin
from blog.models.meeting import Meeting
from blog.models.member import Member
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q, F
from django.db.models import Count
from django.contrib.auth.mixins import PermissionRequiredMixin


class MeetingSignin(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Signin
    fields = ['user']
    template_name = 'blog/signin.html'
    login_url = reverse_lazy('login')
    permission_required = "blog.meeting_gui_can_create"

    def get_initial(self):
        initial = super().get_initial()
        initial['meeting'] = Meeting.objects.filter(start_time__isnull=False, end_time__gte=timezone.now()).order_by(
            'id').last()
        return initial

    def form_valid(self, form):
        form.instance.meeting = Meeting.objects.get(pk=self.kwargs['pk'])

        if form.instance.meeting.start_time > timezone.now():
            return HttpResponse('meeting has not started', status=500)

        if form.instance.meeting.end_time < timezone.now():
            return HttpResponse('meeting has ended', status=500)

        ret = super().form_valid(form)
        return ret

    def get_success_url(self):
        return reverse('blog:signin', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        ctx = super(MeetingSignin, self).get_context_data(**kwargs)
        signins = Signin.objects.filter(meeting=Meeting.objects.get(pk=self.kwargs['pk']), end_time__isnull=True).all()
        usr = Member.objects.annotate(signin_count=Count(F('signin'))).filter(
            ~Q(signin__in=signins) | Q(signin_count=0))
        ctx['form'].fields['user'].queryset = usr
        ctx['meeting'] = Meeting.objects.get(pk=self.kwargs['pk'])
        ctx['signed_in'] = Signin.objects.filter(end_time__isnull=True,
                                                 meeting=Meeting.objects.get(pk=self.kwargs['pk'])).all()
        ctx['pw_form'] = PasswordForm()
        return ctx
