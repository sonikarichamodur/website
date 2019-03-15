from django.db import models
from django.contrib.postgres.fields import HStoreField
from django.core.validators import *


class Year(models.Model):
    """ An FRC Year """
    year = models.IntegerField(primary_key=True, validators=[
        MinValueValidator(1900),
        MaxValueValidator(2100),
    ])


class District(models.Model):
    """ An FRC District for a given year """
    # Internal TBA identifier for this robot.
    key = models.CharField(primary_key=True, max_length=16)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    abbreviation = models.CharField(max_length=255)
    display_name = models.CharField(max_length=1024)


class Team(models.Model):
    # TBA team key with the format `frcXXXX` with `XXXX` representing the team number.
    key = models.CharField(primary_key=True, max_length=16)
    team_number = models.IntegerField(null=False)
    nickname = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024)
    city = models.CharField(max_length=1024)
    state_prov = models.CharField(max_length=1024)
    country = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    postal_code = models.CharField(max_length=1024)
    gmaps_place_id = models.CharField(max_length=1024)
    gmaps_url = models.CharField(max_length=1024)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    location_name = models.CharField(max_length=1024)
    website = models.CharField(max_length=1024)
    rookie_year = models.IntegerField()
    motto = models.CharField(max_length=1024)
    home_championship = HStoreField()


class TeamRobot(models.Model):
    # Internal TBA identifier for this robot.
    key = models.CharField(primary_key=True, max_length=512)

    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Name of the robot as provided by the team.
    robot_name = models.CharField(max_length=512)
