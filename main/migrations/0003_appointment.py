# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150912_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repeat', models.IntegerField(null=True, blank=True)),
                ('studyphase', models.IntegerField(null=True, blank=True)),
                ('appt_date', models.DateField(help_text=b'Format: YYYY-MM-DD', null=True, blank=True)),
                ('appt_time', models.TimeField(help_text=b'Format: HH:MM:SS', null=True, blank=True)),
                ('test_site', models.CharField(max_length=10, blank=True)),
                ('modified_by', models.CharField(max_length=45, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('volunteers', models.ForeignKey(to='main.Volunteer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
