# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro', '0007_auto_20160711_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='price',
            field=models.CharField(blank=True, max_length=80, verbose_name='Цена товара, Сом'),
        ),
    ]