# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-18 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190318_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Название')),
                ('weight', models.CharField(max_length=55, verbose_name='Вес')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.CategoryProducts', verbose_name='Категория')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]