# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('marca', models.CharField(max_length=140)),
                ('cilindros', models.CharField(max_length=140)),
            ],
        ),
    ]