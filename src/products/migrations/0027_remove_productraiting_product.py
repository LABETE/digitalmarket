# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20151216_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productraiting',
            name='product',
        ),
    ]
