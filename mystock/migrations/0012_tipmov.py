# Generated by Django 4.2 on 2024-04-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystock', '0011_item_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipmov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipomov', models.CharField(max_length=20)),
            ],
        ),
    ]