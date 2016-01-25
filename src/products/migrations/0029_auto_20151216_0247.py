# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0028_productraiting_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='products.Product')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='productraiting',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productraiting',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProductRaiting',
        ),
    ]
