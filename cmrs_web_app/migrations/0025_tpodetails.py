# Generated by Django 4.2.5 on 2024-04-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmrs_web_app', '0024_alter_application_options_application_batchyear_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TPODetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('CurrentBatchYear', models.IntegerField()),
            ],
        ),
    ]
