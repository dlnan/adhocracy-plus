# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('liqd_product_partners', '0010_update_helptexts')]

    dependencies = [
        ('a4_candy_partners', '0009_shorten_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.CharField(help_text='max. 400 characters', max_length=400, verbose_name='Short description of your municipality'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='slogan',
            field=models.CharField(blank=True, help_text='max. 200 characters', max_length=200, verbose_name='Slogan'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='title',
            field=models.CharField(default='Beteiligungsplattform', help_text='max. 100 characters', max_length=100),
        ),
    ]