from django.db import models
from django.contrib.postgres.fields import HStoreField, ArrayField
from django.core.validators import *


class Year(models.Model):
    """ An FRC Year """
    year = models.IntegerField(primary_key=True, validators=[
        MinValueValidator(1900),
        MaxValueValidator(2100),
    ])


class District(models.Model):
    """ An FRC District for a given year
    https://github.com/TBA-API/tba-api-client-python/blob/master/docs/DistrictList.md
    """
    # Internal TBA identifier for this robot.
    key = models.CharField(primary_key=True, max_length=16)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    abbreviation = models.CharField(max_length=255)
    display_name = models.CharField(max_length=1024)


class Team(models.Model):
    """
    https://github.com/TBA-API/tba-api-client-python/blob/master/docs/Team.md
    """
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
    """
    https://github.com/TBA-API/tba-api-client-python/blob/master/docs/TeamRobot.md
    """
    # Internal TBA identifier for this robot.
    key = models.CharField(primary_key=True, max_length=512)

    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Name of the robot as provided by the team.
    robot_name = models.CharField(max_length=512)


class Event(models.Model):
    """ An FRC Event
    https://github.com/TBA-API/tba-api-client-python/blob/master/docs/Event.md
    """
    key = models.CharField(primary_key=True, max_length=512)
    name = models.CharField(max_length=1024)
    event_code = models.CharField(max_length=255)
    # event_type = models.IntegerField() #FIXME: Lookup values https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2
    # # district
    # city
    # state_prov
    # country
    # start_date
    # end_date
    # year = models.ForeignKey(Year, on_delete=models.CASCADE)
    # short_name
    # event_type_string
    # week
    # address
    # postal_code
    # gmaps_place_id
    # gmaps_url
    # lat
    # lng
    # location_name
    # timezone
    # website
    # first_event_id
    # first_event_code
    # #webcasts
    # division_keys
    # parent_event_key
    # playoff_type
    # playoff_type_string


class Award(models.Model):
    """
    https://github.com/TBA-API/tba-api-client-python/blob/master/docs/Award.md
    """
    name = models.CharField(max_length=1024)
    award_type = models.CharField(max_length=1024)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)


class AwardRecipient(models.Model):
    """
    https://github.com/TBA-API/tba-api-client-python/blob/master/docs/AwardRecipient.md
    """
    award = models.ForeignKey(Award, on_delete=models.CASCADE, related_name='recipient_list')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    awardee = models.CharField(max_length=1024)


class DistrictRanking(models.Model):
    """
    https://github.com/TBA-API/tba-api-client-python/blob/master/docs/DistrictRanking.md
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rank = models.IntegerField()
    rookie_bonus = models.IntegerField()
    point_total = models.IntegerField()
    # event_points


class DistrictRankingEventPoints(models.Model):
    """
    https://github.com/TBA-API/tba-api-client-python/blob/master/docs/DistrictRankingEventPoints.md
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    district_ranking = models.ForeignKey(DistrictRanking, on_delete=models.CASCADE)
    district_cmp = models.BooleanField()
    alliance_points = models.IntegerField()
    award_points = models.IntegerField()
    qual_points = models.IntegerField()
    elim_points = models.IntegerField()
    total = models.IntegerField()
