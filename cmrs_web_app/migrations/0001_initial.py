# Generated by Django 4.2.5 on 2023-12-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('Title', models.CharField(max_length=50, verbose_name='Title')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
