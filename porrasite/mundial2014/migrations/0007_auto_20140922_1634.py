# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial2014', '0006_auto_20140922_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partido',
            name='local',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='local_id',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='visitante',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='visitante_id',
        ),
    ]
