# Generated by Django 3.1 on 2022-08-19 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incharge_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=300, unique=True)),
                ('images', models.ImageField(upload_to='photos/products')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100, unique=True)),
                ('room_no', models.IntegerField()),
                ('description', models.TextField(max_length=300, unique=True)),
                ('images', models.ImageField(upload_to='photos/products')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('incharge_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='issue.incharge')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_priority', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='issue.room')),
            ],
        ),
    ]
