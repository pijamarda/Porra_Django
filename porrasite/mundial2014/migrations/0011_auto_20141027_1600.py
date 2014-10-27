# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial2014', '0010_auto_20141027_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='e1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='e2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
