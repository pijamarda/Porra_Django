# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial2014', '0008_auto_20140922_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='a1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rank',
            name='a2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rank',
            name='b1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rank',
            name='b2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
