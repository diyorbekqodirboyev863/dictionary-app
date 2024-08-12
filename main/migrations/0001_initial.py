# Generated by Django 5.1 on 2024-08-12 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('to_process', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('to_process', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en', models.CharField(max_length=255, verbose_name='English')),
                ('uz', models.CharField(blank=True, max_length=255, null=True, verbose_name='Uzbek')),
                ('ru', models.CharField(max_length=255, verbose_name='Russian')),
                ('en_pro', models.CharField(blank=True, max_length=255, null=True)),
                ('ru_pro', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('to_process', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.term')),
            ],
        ),
    ]