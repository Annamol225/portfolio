# Generated by Django 3.2.22 on 2024-01-15 15:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('bgimg', models.ImageField(blank=True, null=True, upload_to='photo')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=40)),
                ('selfdesc', models.TextField()),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=40)),
                ('edu', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('skill', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]