# Generated by Django 2.1.7 on 2019-09-28 19:57

import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('award_type', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='AwardRecipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awardee', models.CharField(max_length=1024)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_list',
                                            to='scout.Award')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('key', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('rookie_bonus', models.IntegerField()),
                ('point_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DistrictRankingEventPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_cmp', models.BooleanField()),
                ('alliance_points', models.IntegerField()),
                ('award_points', models.IntegerField()),
                ('qual_points', models.IntegerField()),
                ('elim_points', models.IntegerField()),
                ('total', models.IntegerField()),
                ('district_ranking',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.DistrictRanking')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('key', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024)),
                ('event_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('key', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('team_number', models.IntegerField()),
                ('nickname', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
                ('city', models.CharField(max_length=1024)),
                ('state_prov', models.CharField(max_length=1024)),
                ('country', models.CharField(max_length=1024)),
                ('address', models.CharField(max_length=1024)),
                ('postal_code', models.CharField(max_length=1024)),
                ('gmaps_place_id', models.CharField(max_length=1024)),
                ('gmaps_url', models.CharField(max_length=1024)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('location_name', models.CharField(max_length=1024)),
                ('website', models.CharField(max_length=1024)),
                ('rookie_year', models.IntegerField()),
                ('motto', models.CharField(max_length=1024)),
                ('home_championship', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamRobot',
            fields=[
                ('key', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('robot_name', models.CharField(max_length=512)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False,
                                             validators=[django.core.validators.MinValueValidator(1900),
                                                         django.core.validators.MaxValueValidator(2100)])),
            ],
        ),
        migrations.AddField(
            model_name='teamrobot',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.Year'),
        ),
        migrations.AddField(
            model_name='districtrankingeventpoints',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.Event'),
        ),
        migrations.AddField(
            model_name='districtranking',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.Team'),
        ),
        migrations.AddField(
            model_name='district',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.Year'),
        ),
        migrations.AddField(
            model_name='awardrecipient',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.Team'),
        ),
        migrations.AddField(
            model_name='award',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.Event'),
        ),
        migrations.AddField(
            model_name='award',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scout.Year'),
        ),
    ]
