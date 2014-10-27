# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial2014', '0009_auto_20141027_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='c1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='c2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='d1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='d2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='f1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='f2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='g1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='g2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='h1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rank',
            name='h2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rank',
            name='a1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rank',
            name='a2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rank',
            name='b1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rank',
            name='b2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rank',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]
