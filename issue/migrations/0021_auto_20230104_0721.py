# Generated by Django 3.1 on 2023-01-04 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0020_token_is_missed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='room_no',
            new_name='room',
        ),
    ]
