# Generated by Django 4.2.5 on 2023-09-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Sin descripción'),
        ),
    ]