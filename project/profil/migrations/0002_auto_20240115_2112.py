# Generated by Django 3.2.22 on 2024-01-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skl', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='profil',
            name='skill',
            field=models.ManyToManyField(blank=True, to='profil.skills'),
        ),
    ]
