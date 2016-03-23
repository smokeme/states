# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_statecities_capital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statecities',
            old_name='city_latitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='statecities',
            old_name='city_longitude',
            new_name='longitude',
        ),
        migrations.RemoveField(
            model_name='statecities',
            name='city_state',
        ),
    ]
