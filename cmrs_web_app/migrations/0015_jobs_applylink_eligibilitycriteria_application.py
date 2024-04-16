# Generated by Django 4.2.5 on 2024-04-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmrs_web_app', '0014_company_alter_jobs_options_jobs_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='ApplyLink',
            field=models.URLField(null=True),
        ),
        migrations.CreateModel(
            name='EligibilityCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_cgpa', models.FloatField(null=True)),
                ('max_backlog_count', models.IntegerField(null=True)),
                ('skills_required', models.CharField(max_length=250, null=True)),
                ('min_twelth_percentage', models.FloatField(null=True)),
                ('min_tenth_cgpa', models.FloatField(null=True)),
                ('no_gap_year', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmrs_web_app.jobs')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateField(auto_now_add=True)),
                ('is_accepted', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmrs_web_app.jobs')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmrs_web_app.student')),
            ],
        ),
    ]