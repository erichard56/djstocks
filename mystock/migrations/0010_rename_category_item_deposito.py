# Generated by Django 4.2 on 2024-04-13 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystock', '0009_alter_log_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='category',
            new_name='deposito',
        ),
    ]
