# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0012_auto_20151212_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='managers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='managers_products', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
