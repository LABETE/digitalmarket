# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20151213_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_active',
            field=models.BooleanField(default=True),
        ),
    ]
