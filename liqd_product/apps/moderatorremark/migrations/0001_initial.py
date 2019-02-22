# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 08:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeratorRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('item_object_id', models.PositiveIntegerField()),
                ('remark', models.CharField(blank=True, max_length=200, verbose_name='Remark')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'meinberlin_moderatorremark_moderatorremark',
            },
        ),
        migrations.AlterUniqueTogether(
            name='moderatorremark',
            unique_together=set([('item_content_type', 'item_object_id', 'id')]),
        ),
    ]
