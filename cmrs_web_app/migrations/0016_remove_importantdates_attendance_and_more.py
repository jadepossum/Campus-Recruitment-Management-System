# Generated by Django 4.2.5 on 2024-04-15 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmrs_web_app', '0015_jobs_applylink_eligibilitycriteria_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importantdates',
            name='Attendance',
        ),
        migrations.RemoveField(
            model_name='importantdates',
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentFeedback',
        ),
    ]
