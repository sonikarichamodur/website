# Generated by Django 2.2.6 on 2019-11-03 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0022_auto_20191103_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMember',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=4096, verbose_name='member name')),
                ('slack', models.CharField(blank=True, max_length=4096, null=True, verbose_name='slack id')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='user added')),
                ('modified', models.DateTimeField(blank=True, editable=False, verbose_name='user modified')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True,
                                           on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical member',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMeeting',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, editable=False, verbose_name='meeting start time')),
                ('end_time', models.DateTimeField(default=None, null=True, verbose_name='meeting end time')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True,
                                           on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical meeting',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
