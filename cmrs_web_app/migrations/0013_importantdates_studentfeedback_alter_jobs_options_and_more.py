# Generated by Django 4.2.5 on 2024-04-12 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmrs_web_app', '0012_student_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Description', models.CharField(max_length=250)),
                ('EventTitle', models.CharField(max_length=250)),
                ('Attendance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhaseNo', models.IntegerField(null=True)),
                ('PhaseTitle', models.CharField(max_length=50, null=True)),
                ('PhaseFeedback', models.TextField(null=True)),
                ('Rating', models.IntegerField(null=True)),
                ('DifficultyLevel', models.CharField(max_length=50, null=True)),
                ('Suggestions', models.TextField(null=True)),
                ('WouldRecommend', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='jobs',
            name='Deadline',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='Location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='Prerequisites',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='RequiredSkills',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='Salary',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='Status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='Description',
            field=models.TextField(null=True, verbose_name='Desc'),
        ),
        migrations.DeleteModel(
            name='UserLogin',
        ),
        migrations.AddField(
            model_name='studentfeedback',
            name='Job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmrs_web_app.jobs'),
        ),
        migrations.AddField(
            model_name='studentfeedback',
            name='RollNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmrs_web_app.student'),
        ),
        migrations.AddField(
            model_name='importantdates',
            name='Job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmrs_web_app.jobs'),
        ),
        migrations.AddField(
            model_name='importantdates',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmrs_web_app.student'),
        ),
        migrations.AlterUniqueTogether(
            name='studentfeedback',
            unique_together={('Job', 'RollNumber', 'PhaseNo')},
        ),
    ]