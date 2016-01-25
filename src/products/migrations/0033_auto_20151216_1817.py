# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0032_curatedproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuratedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('section_name', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(blank=True, to='products.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curated Products',
                'verbose_name_plural': 'Curated Products',
            },
        ),
        migrations.RemoveField(
            model_name='curatedproduct',
            name='products',
        ),
        migrations.RemoveField(
            model_name='curatedproduct',
            name='user',
        ),
        migrations.DeleteModel(
            name='CuratedProduct',
        ),
    ]
