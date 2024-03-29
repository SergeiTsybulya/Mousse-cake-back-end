# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-05-05 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import product.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Название начинки')),
                ('description', models.CharField(max_length=250, verbose_name='Описание начинки')),
                ('photo', stdimage.models.StdImageField(max_length=255, null=True, upload_to=product.models.make_upload_path_filling, verbose_name='Фото начинки')),
                ('ingradient', models.ManyToManyField(blank=True, to='product.Ingredient')),
            ],
            options={
                'verbose_name': 'Начинка',
                'verbose_name_plural': 'Начинки',
            },
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Категория сладостей'),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Категория сладостей'),
        ),
        migrations.AddField(
            model_name='categoryproducts',
            name='name_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Категория сладостей'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uk',
            field=models.CharField(max_length=55, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='filling',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Filling', verbose_name='Начинка'),
        ),
    ]
