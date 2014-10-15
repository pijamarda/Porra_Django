# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial2014', '0004_equipo_equipo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo_id', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('team1', models.IntegerField()),
                ('team2', models.IntegerField()),
                ('team3', models.IntegerField()),
                ('team4', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
