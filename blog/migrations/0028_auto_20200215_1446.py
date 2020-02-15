# Generated by Django 3.0.3 on 2020-02-15 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0027_load_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False)),
                ('display_name', models.CharField(blank=True, max_length=255, unique=True)),
            ],
        ),
    ]
