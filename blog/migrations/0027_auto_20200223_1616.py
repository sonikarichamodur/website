# Generated by Django 2.2.10 on 2020-02-23 21:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0026_auto_20200218_2148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'permissions': (('meeting_gui_can_create', 'Can create new meetings via the GUI'),
                                     ('meeting_gui_can_view', 'Can view meeting/member stats via the GUI'))},
        ),
    ]
