# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='value1',
            field=models.CharField(blank=True, help_text='Product.subcategory.feature1', max_length=80, verbose_name='Характеристика 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='value2',
            field=models.CharField(blank=True, max_length=80, verbose_name='Характеристика 1'),
        ),
    ]