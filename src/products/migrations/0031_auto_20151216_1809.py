# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_curatedproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curatedproducts',
            name='products',
        ),
        migrations.RemoveField(
            model_name='curatedproducts',
            name='user',
        ),
        migrations.DeleteModel(
            name='CuratedProducts',
        ),
    ]
