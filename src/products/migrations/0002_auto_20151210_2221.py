# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Default Value'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=100, default=9.99, decimal_places=2),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(max_digits=100, default=9.99, decimal_places=2),
        ),
    ]
