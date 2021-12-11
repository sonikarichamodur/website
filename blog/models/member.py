from django.contrib.auth.models import User
from django.db import models
from blog.models.users import Details
from blog.models.post import Post
from simple_history.models import HistoricalRecords
from datetime import timedelta
from django.db.models import F, Q, Sum


class Member(models.Model):
    TEAM = (
        ("None", "None"),
        ("Software", "Software"),
        ("CAD/Manufacturing", "CAD/Manufacturing"),
        ("Outreach", "Outreach"),
        ("Strategy", "Strategy"),
        ("Safety", "Safety"),
        ("Helping Hands", "Helping Hands"),
        ("Sponsorship", "Sponsorship"),
        ("Graphics/Spirit", "Graphics/Spirit"),
        ("Comun/Website", "Comun/Website"),
        ("Visuals", "Visuals"),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField('member name', max_length=4096)
    slack = models.CharField('slack id', max_length=4096, blank=True, null=True)
    team = models.CharField('team name', max_length=255, blank=False, null=False, choices=TEAM, default="None")
    created = models.DateTimeField('user added', auto_now_add=True)
    modified = models.DateTimeField('user modified', auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.team} | {self.name}"

    def stats(self, pct_no_end=0, q=Q()):
        """ The member's hours """
        ttl_hours = timedelta(seconds=0)
        skipped = 0
        for signin in self.signin_set.filter(q).all():
            if signin.meeting.end_time is None:
                # meeting is on going
                continue
            end = signin.end_time
            if not signin.isvalid():
                skipped += 1
                continue
            if end is None:
                # Never signed out - use pct_no_end
                if pct_no_end:
                    if pct_no_end > 100 or pct_no_end < 0:
                        raise ValueError("Bad pct_no_end value")
                    max_hours = signin.meeting.end_time - signin.start_time
                    ttl_hours *= pct_no_end / 100
                    continue
                else:
                    skipped += 1
                    continue
            else:
                ttl_hours += signin.end_time - signin.start_time
        return dict(
            ttl=ttl_hours,
            skipped=skipped,
        )
