# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-14 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(db_index=True, max_length=16, unique=True, verbose_name='Phone_num')),
                ('nickname', models.CharField(max_length=32, verbose_name='Nick_name')),
                ('sex', models.CharField(choices=[('male', 'man'), ('female', 'woman')], max_length=8, verbose_name='Sex')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('avatar', models.CharField(max_length=256, verbose_name='Avatar')),
                ('location', models.Field(choices=[('SH', 'Shanghai'), ('BJ', 'Beijing'), ('HN', 'Henan')], max_length=64, verbose_name='Location')),
            ],
        ),
    ]
