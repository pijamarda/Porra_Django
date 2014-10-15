# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial2014', '0003_auto_20140922_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='equipo_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
