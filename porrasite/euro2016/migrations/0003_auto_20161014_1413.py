# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('euro2016', '0002_auto_20150806_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankeuro2016',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
