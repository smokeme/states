# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160315_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecapital',
            name='state',
            field=models.ForeignKey(blank=True, to='main.State', null=True),
        ),
        migrations.AlterField(
            model_name='statecities',
            name='state',
            field=models.ForeignKey(blank=True, to='main.State', null=True),
        ),
    ]
