# Generated by Django 3.1 on 2023-01-04 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='room_no',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='assignroom',
            old_name='room_no',
            new_name='room',
        ),
    ]
