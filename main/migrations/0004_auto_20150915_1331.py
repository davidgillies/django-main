# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_appointment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='surgery',
            options={'verbose_name': 'Surgery', 'verbose_name_plural': 'Surgeries'},
        ),
    ]
