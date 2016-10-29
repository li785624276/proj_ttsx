# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goodKinds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kinds', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='goodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to=b'demo/media')),
                ('price', models.FloatField(default=0.0)),
                ('intro', models.TextField()),
                ('describe', tinymce.models.HTMLField()),
                ('kucunliang', models.IntegerField(default=100)),
                ('goodKinds', models.ForeignKey(to='demo.goodKinds')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('state', models.BooleanField(default=False)),
                ('totalprice', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='order_goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_num', models.IntegerField()),
                ('cur_price', models.IntegerField()),
                ('goods_id', models.ForeignKey(to='demo.goodsInfo')),
                ('order_id', models.ForeignKey(to='demo.order')),
            ],
        ),
        migrations.CreateModel(
            name='shoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_num', models.IntegerField()),
                ('totalprice', models.FloatField(default=0.0)),
                ('goods_id', models.ForeignKey(to='demo.goodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('passwd', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user_addr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=45)),
                ('postcode', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(to='demo.user')),
            ],
        ),
        migrations.CreateModel(
            name='user_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_id', models.ForeignKey(to='demo.goodsInfo')),
                ('user_id', models.ForeignKey(to='demo.user')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user_id',
            field=models.ForeignKey(to='demo.user'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(to='demo.user'),
        ),
    ]
