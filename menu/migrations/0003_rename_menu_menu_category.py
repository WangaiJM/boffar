# Generated by Django 5.0.2 on 2024-02-17 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu',
            new_name='category',
        ),
    ]