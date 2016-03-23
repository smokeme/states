# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160314_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecapital',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='population',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='state',
            field=models.ForeignKey(blank=True, to='main.State', null=True),
        ),
    ]
