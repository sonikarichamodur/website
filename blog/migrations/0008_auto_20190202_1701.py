# Generated by Django 2.1.5 on 2019-02-02 22:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0007_maintext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintext',
            name='link',
        ),
        migrations.RemoveField(
            model_name='maintext',
            name='title',
        ),
        migrations.RemoveField(
            model_name='maintext',
            name='user',
        ),
    ]
