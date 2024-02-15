# Generated by Django 5.0.2 on 2024-02-14 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('demoapp', '0002_category_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoapp.product')),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
    ]
