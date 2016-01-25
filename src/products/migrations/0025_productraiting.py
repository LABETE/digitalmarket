# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0024_auto_20151215_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRaiting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('raiting', models.IntegerField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('products', models.ManyToManyField(to='products.Product')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
