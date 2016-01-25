# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0016_myproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('height', models.CharField(max_length=20, blank=True, null=True)),
                ('width', models.CharField(max_length=20, blank=True, null=True)),
                ('media', models.ImageField(upload_to=products.models.download_media_location, blank=True, null=True, height_field='height', width_field='width')),
                ('product', models.ForeignKey(to='products.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
