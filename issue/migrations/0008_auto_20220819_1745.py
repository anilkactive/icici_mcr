# Generated by Django 3.1 on 2022-08-19 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0007_auto_20220819_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='room_no',
            new_name='room_name',
        ),
    ]
