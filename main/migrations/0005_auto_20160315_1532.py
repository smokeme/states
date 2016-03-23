# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160314_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.IntegerField(null=True, blank=True)),
                ('city_latitude', models.FloatField(null=True, blank=True)),
                ('city_longitude', models.FloatField(null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('city_state', models.CharField(max_length=2, null=True, blank=True)),
                ('county', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, blank=True, to='main.State'),
        ),
        migrations.AddField(
            model_name='statecities',
            name='capital',
            field=models.OneToOneField(null=True, blank=True, to='main.StateCapital'),
        ),
        migrations.AddField(
            model_name='statecities',
            name='state',
            field=models.OneToOneField(null=True, blank=True, to='main.State'),
        ),
    ]
