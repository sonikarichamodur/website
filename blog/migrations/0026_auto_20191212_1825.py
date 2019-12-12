from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0025_auto_20191123_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmember',
            name='team',
            field=models.CharField(choices=[('None', 'None'), ('Programming/Electrical', 'Programming/Electrical'),
                                            ('CAD/Manufacturing', 'CAD/Manufacturing'), ('Outreach', 'Outreach'),
                                            ('Strategy', 'Strategy'), ('Safety', 'Safety'),
                                            ('Helping Hands', 'Helping Hands'), ('Sponsorship', 'Sponsorship'),
                                            ('Graphics/Spirit', 'Graphics/Spirit'), ('Comun/Website', 'Comun/Website'),
                                            ('Visuals', 'Visuals')], default='None', max_length=255,
                                   verbose_name='team name')),
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.CharField(choices=[('None', 'None'), ('Programming/Electrical', 'Programming/Electrical'),
                                            ('CAD/Manufacturing', 'CAD/Manufacturing'), ('Outreach', 'Outreach'),
                                            ('Strategy', 'Strategy')
                , ('Safety', 'Safety'), ('Helping Hands', 'Helping Hands'), ('Sponsorship', 'Sponsorship'),
                                            ('Graphics/Spirit', 'Graphics/Spirit'), ('Comun/Website', 'Comun/Website'),
                                            ('Visuals', 'Visuals')], default='None', max_length=255,
                                   verbose_name='team name'),
        ),
        migrations.CreateModel(
            name='MeetingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subteam', models.CharField(
                    choices=[('None', 'None'), ('Programming/Electrical', 'Programming/Electrical'),
                             ('CAD/Manufacturing', 'CAD/Manufacturing'), ('Outreach', 'Outreach'),
                             ('Strategy', 'Strategy'),
                             ('Safety', 'Safety'), ('Helping Hands', 'Helping Hands'), ('Sponsorship', 'Sponsorship'),
                             ('Graphics / Spirit', 'Graphics / Spirit'), ('Comun / Website', 'Comun / Website'),
                             ('Visuals', 'Visuals')], default='None', max_length=255, verbose_name='team name')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Meeting')),
            ],
        ),
    ]
