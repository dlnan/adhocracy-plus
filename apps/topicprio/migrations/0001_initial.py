# Generated by Django 2.2.6 on 2019-11-08 12:03

import adhocracy4.categories.fields
import adhocracy4.images.fields
import autoslug.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a4labels', '0001_initial'),
        ('a4modules', '0004_description_maxlength_512'),
        ('a4categories', '0002_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('item_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='a4_candy_topicprio_topic', serialize=False, to='a4modules.Item')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=120, verbose_name='Title')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', adhocracy4.images.fields.ConfiguredImageField('idea_image', blank=True, upload_to='ideas/images', verbose_name='Add image')),
                ('category', adhocracy4.categories.fields.CategoryField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4categories.Category', verbose_name='Category')),
                ('labels', models.ManyToManyField(related_name='a4_candy_topicprio_topic_label', to='a4labels.Label', verbose_name='Labels')),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=('a4modules.item',),
        ),
    ]