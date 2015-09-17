# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('addr1', models.CharField(max_length=45, blank=True)),
                ('addr2', models.CharField(max_length=45, blank=True)),
                ('town', models.CharField(max_length=45, blank=True)),
                ('county', models.CharField(max_length=45, blank=True)),
                ('postcode', models.CharField(max_length=45, blank=True)),
                ('telephone', models.CharField(max_length=12, blank=True)),
                ('admin_contact_name', models.CharField(max_length=45, blank=True)),
                ('admin_contact_number', models.CharField(max_length=45, blank=True)),
                ('hscic_code', models.CharField(max_length=45, blank=True)),
                ('area', models.CharField(max_length=45, blank=True)),
                ('modified_by', models.CharField(max_length=45, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('surgeriescol', models.CharField(max_length=45, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='addr1',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='addr2',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='county',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='diabetes_diagnosed',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'True'), (2, b'False'), (3, b'None')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='dob',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='email',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='home_tel',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='initials',
            field=models.CharField(max_length=5, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='mobile',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='modified',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='modified_by',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='moved_away',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'True'), (2, b'False'), (3, b'None')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='nhs_no',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='phase1_comment',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='phase2_comment',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='postcode',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='reason',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='sex',
            field=models.CharField(blank=True, max_length=1, choices=[(b'M', b'M'), (b'F', b'F')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='surgeries',
            field=models.ForeignKey(blank=True, to='main.Surgery', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='title',
            field=models.CharField(blank=True, max_length=12, choices=[(b'Mr', b'Mr'), (b'Mrs', b'Mrs'), (b'Ms', b'Ms'), (b'Miss', b'Miss'), (b'Dr', b'Dr'), (b'Prof', b'Prof')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='town',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='work_tel',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
    ]
