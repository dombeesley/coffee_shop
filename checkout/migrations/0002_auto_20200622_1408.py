# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-22 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40, verbose_name='Country:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=40, verbose_name='County:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='Your full name:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Your phone number:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, verbose_name='Post code:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(max_length=40, verbose_name='Address (Line 1):'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(max_length=40, verbose_name='Address (Line 2):'),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(max_length=40, verbose_name='Town or city:'),
        ),
    ]
