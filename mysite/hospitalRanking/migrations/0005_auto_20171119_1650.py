# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalRanking', '0004_auto_20171119_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normalized_payment',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospitalRanking.Hospital'),
        ),
    ]
