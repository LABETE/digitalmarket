# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20151213_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.ImageField(null=True, upload_to=products.models.download_media_location, blank=True, storage=django.core.files.storage.FileSystemStorage(location='/home/labete/Desktop/dm/static_cdn/protected')),
        ),
    ]
