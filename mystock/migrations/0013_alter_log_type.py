# Generated by Django 4.2 on 2024-04-17 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystock', '0012_tipmov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mystock.tipmov'),
        ),
    ]
