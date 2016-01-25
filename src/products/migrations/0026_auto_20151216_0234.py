# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_productraiting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productraiting',
            name='products',
        ),
        migrations.AddField(
            model_name='productraiting',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
