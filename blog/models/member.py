from django.contrib.auth.models import User
from django.db import models
from blog.models.users import Details
from blog.models.post import Post
from simple_history.models import HistoricalRecords


class Member(models.Model):
    TEAM = (
        ("None", "None"),
        ("Programming/Electrical", "Programming/Electrical"),
        ("CAD/Manufacturing", "CAD/Manufacturing"),
        ("Outreach", "Outreach"),
        ("Strategy", "Strategy"),
        ("Safety", "Safety"),
        ("Helping Hands", "Helping Hands"),
        ("Sponsorship","Sponsorship"),
        ("Graphics/Spirit","Graphics/Spirit"),
        ("Comun/Website","Comun/Website"),
        ("Visuals","Visuals"),
       # ("","",), #Dr. T's daughters

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
