# Generated by Django 3.1 on 2022-08-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0009_auto_20220819_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='tok_no',
            field=models.IntegerField(null=True),
        ),
    ]
