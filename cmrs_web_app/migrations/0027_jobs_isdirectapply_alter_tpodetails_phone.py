# Generated by Django 4.2.5 on 2024-05-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmrs_web_app', '0026_alter_tpodetails_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='IsDirectApply',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='tpodetails',
            name='Phone',
            field=models.CharField(max_length=10),
        ),
    ]
