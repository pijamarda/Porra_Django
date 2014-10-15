# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial2014', '0005_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='team3',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='team4',
        ),
        migrations.AddField(
            model_name='equipo',
            name='grupo',
            field=models.ForeignKey(default=1, to='mundial2014.Grupo'),
            preserve_default=False,
        ),
    ]
