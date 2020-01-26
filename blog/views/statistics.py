from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.shortcuts import render

from blog.models.member import Member

from blog.models.signin import Signin
import datetime


@login_required
def stats(request):
    member_hours = []
    for member in Member.objects.all():
        hours = Signin.objects.filter(member, start_time__gte=datetime.datetime(2020, 1, 1)) \
            .annotate(signin_time=F('end_time') - F('start_time')).aggregate(Sum('signin_time')).values()[0]

        if hours:
            member_hours.append((member.name, hours))

    member_hours.sort(reverse=True, key=lambda x: x[1])

    return render(request, 'blog/statistics.html', {'members': member_hours})
