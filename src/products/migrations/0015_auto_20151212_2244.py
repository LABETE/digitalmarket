# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/labete/Desktop/dm/static_cdn/protected'), blank=True, upload_to=products.models.download_media_location, null=True),
        ),
    ]
