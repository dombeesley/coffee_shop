# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-25 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='username',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
