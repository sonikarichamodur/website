# Generated by Django 2.1.5 on 2019-02-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_files'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'verbose_name': 'File', 'verbose_name_plural': 'Files'},
        ),
        migrations.AddField(
            model_name='files',
            name='path',
            field=models.FilePathField(default=None),
            preserve_default=False,
        ),
    ]
