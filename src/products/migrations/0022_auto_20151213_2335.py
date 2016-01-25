# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_thumbnail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='user',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='type',
            field=models.CharField(default='hd', max_length=20, choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')]),
        ),
    ]
