# Generated by Django 4.2 on 2024-04-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystock', '0010_rename_category_item_deposito'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imagen',
            field=models.ImageField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
