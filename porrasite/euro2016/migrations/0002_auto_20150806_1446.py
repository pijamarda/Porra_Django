# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euro2016', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rankeuro2016',
            name='g1',
        ),
        migrations.RemoveField(
            model_name='rankeuro2016',
            name='g2',
        ),
        migrations.RemoveField(
            model_name='rankeuro2016',
            name='h1',
        ),
        migrations.RemoveField(
            model_name='rankeuro2016',
            name='h2',
        ),
    ]
