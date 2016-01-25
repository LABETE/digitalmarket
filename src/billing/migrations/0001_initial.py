# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0022_auto_20151213_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(null=True, max_digits=100, default=9.99, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('success', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
