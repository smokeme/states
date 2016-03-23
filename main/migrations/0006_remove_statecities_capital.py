# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160315_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statecities',
            name='capital',
        ),
    ]
