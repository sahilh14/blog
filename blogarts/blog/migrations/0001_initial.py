# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'namE')),
                ('email', models.EmailField(max_length=254, verbose_name=b'E-maIl')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'TitLe')),
                ('content', models.TextField(verbose_name=b'cONtEnt')),
                ('published', models.DateTimeField(verbose_name=b'WRItten ON')),
                ('author', models.ForeignKey(verbose_name=b'WriTTen bY', to='blog.Author')),
            ],
        ),
    ]
