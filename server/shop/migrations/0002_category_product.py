# Generated by Django 5.0 on 2023-12-11 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this model should be treated as active. Unselect this instead of deleting models.', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this model should be treated as active. Unselect this instead of deleting models.', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='Description about the product.', null=True)),
                ('price', models.FloatField(default=0.0, help_text='Price for this product.')),
                ('category', models.ForeignKey(help_text='The category this product belongs to.', on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
