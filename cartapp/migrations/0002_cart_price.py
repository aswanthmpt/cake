# Generated by Django 5.0.2 on 2024-02-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=2222, max_digits=10),
            preserve_default=False,
        ),
    ]
