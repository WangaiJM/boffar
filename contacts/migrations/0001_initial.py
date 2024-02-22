# Generated by Django 5.0.2 on 2024-02-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('queried_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
