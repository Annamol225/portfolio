# Generated by Django 3.2.22 on 2024-01-15 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0002_auto_20240115_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='skill',
        ),
        migrations.DeleteModel(
            name='skills',
        ),
    ]