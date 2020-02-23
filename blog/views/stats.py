from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, Http404
from django.contrib.auth.decorators import permission_required
from blog.models.member import Member
from blog.models.meeting import Meeting
from blog.models.signin import Signin
from django.db.models import F, Q, Sum
from ..forms import StatsForm


@permission_required("meeting_gui_can_view")
def stats(request):
    form = StatsForm(request.POST)
    if form.is_valid():
        by_hours = []
        by_name = []
        start = form.cleaned_data.get('start', None)
        end = form.cleaned_data.get('end', None)
        pct_end = form.cleaned_data['pct_end']
        signin_q = Q()
        if start:
            signin_q = signin_q and Q(start_time__lte=start)
        if end:
            signin_q = signin_q and Q(meeting__end_time__lte=end)

        for member in Member.objects.all():
            by_hours.append((member, member.stats(pct_end, signin_q)))
            by_name.append(member)

        by_hours.sort(key=lambda x: x[1]['ttl'])
        by_name.sort(key=lambda x: x.name)

        return render(request, 'blog/stats.html', {
            "by_hours": by_hours,
            "by_name": by_name,
            "start": start,
            "end": end,
            "form": form,
        })
    return render(request, 'blog/stats.html', {
        "form": form,
    })
