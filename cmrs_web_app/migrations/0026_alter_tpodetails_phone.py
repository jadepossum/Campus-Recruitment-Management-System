# Generated by Django 4.2.5 on 2024-04-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmrs_web_app', '0025_tpodetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tpodetails',
            name='Phone',
            field=models.IntegerField(),
        ),
    ]
