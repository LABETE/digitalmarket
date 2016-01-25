# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20151210_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(max_digits=100, blank=True, null=True, default=6.99, decimal_places=2),
        ),
    ]
