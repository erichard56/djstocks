# Generated by Django 4.2 on 2024-04-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystock', '0006_alter_log_type_alter_usuario_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
