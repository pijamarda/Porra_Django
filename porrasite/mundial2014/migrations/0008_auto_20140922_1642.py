# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial2014', '0007_auto_20140922_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='local',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partido',
            name='local_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partido',
            name='visitante',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partido',
            name='visitante_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
