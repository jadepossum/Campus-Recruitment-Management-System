# Generated by Django 4.2.5 on 2024-04-12 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmrs_web_app', '0013_importantdates_studentfeedback_alter_jobs_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Industry', models.CharField(max_length=100)),
                ('Size', models.IntegerField()),
                ('Description', models.TextField(null=True)),
                ('FoundedDate', models.DateField(null=True)),
                ('Website', models.URLField(null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={},
        ),
        migrations.AddField(
            model_name='jobs',
            name='Company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='ExperienceLevel',
            field=models.CharField(choices=[('EN', 'Entry Level'), ('IN', 'Intermediate'), ('EX', 'Experienced')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='JobType',
            field=models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('IN', 'Internship')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='PostedDate',
            field=models.DateField(default=datetime.date(2023, 12, 12)),
        ),
    ]
