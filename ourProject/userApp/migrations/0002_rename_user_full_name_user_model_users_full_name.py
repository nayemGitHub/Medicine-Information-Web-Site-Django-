# Generated by Django 5.0 on 2024-01-11 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_model',
            old_name='user_full_name',
            new_name='users_full_name',
        ),
    ]
