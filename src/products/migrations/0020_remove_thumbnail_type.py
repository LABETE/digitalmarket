# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20151213_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='type',
        ),
    ]
