# Generated by Django 4.2 on 2024-04-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystock', '0015_alter_item_price_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='price_venta',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
