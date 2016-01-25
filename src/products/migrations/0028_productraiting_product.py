# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_remove_productraiting_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productraiting',
            name='product',
            field=models.ForeignKey(default=1, to='products.Product'),
            preserve_default=False,
        ),
    ]
