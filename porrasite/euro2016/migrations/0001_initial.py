# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('equipo_id', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('grupo_id', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PartidoEuro2016',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('partido_id', models.IntegerField()),
                ('local_id', models.IntegerField()),
                ('visitante_id', models.IntegerField()),
                ('local', models.IntegerField()),
                ('visitante', models.IntegerField()),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RankEuro2016',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('puntos', models.IntegerField(default=0)),
                ('a1', models.IntegerField(default=0)),
                ('a2', models.IntegerField(default=0)),
                ('b1', models.IntegerField(default=0)),
                ('b2', models.IntegerField(default=0)),
                ('c1', models.IntegerField(default=0)),
                ('c2', models.IntegerField(default=0)),
                ('d1', models.IntegerField(default=0)),
                ('d2', models.IntegerField(default=0)),
                ('e1', models.IntegerField(default=0)),
                ('e2', models.IntegerField(default=0)),
                ('f1', models.IntegerField(default=0)),
                ('f2', models.IntegerField(default=0)),
                ('g1', models.IntegerField(default=0)),
                ('g2', models.IntegerField(default=0)),
                ('h1', models.IntegerField(default=0)),
                ('h2', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='grupo',
            field=models.ForeignKey(to='euro2016.Grupo'),
        ),
    ]
