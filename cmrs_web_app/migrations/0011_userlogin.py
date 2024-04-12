# Generated by Django 4.2.5 on 2024-04-08 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmrs_web_app', '0010_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('password', models.CharField(max_length=30, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cmrs_web_app.student')),
            ],
        ),
    ]