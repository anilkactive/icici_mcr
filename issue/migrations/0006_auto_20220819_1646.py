# Generated by Django 3.1 on 2022-08-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0005_auto_20220819_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incharge',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
