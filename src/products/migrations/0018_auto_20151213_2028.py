# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='user',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='type',
            field=models.CharField(choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')], max_length=20, default='hd'),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='media',
            field=models.ImageField(blank=True, width_field='width', height_field='height', null=True, upload_to=products.models.thumbnail_location),
        ),
    ]
