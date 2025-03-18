# Generated by Django 5.1.4 on 2025-01-30 10:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='joined',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='experience_years',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='notifications_enabled',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='rating',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='role',
            field=models.CharField(blank=True, choices=[('employee', 'Employee'), ('manager', 'Manager'), ('management', 'Management'), ('administrator', 'Administrator')], default='employee', max_length=20, null=True),
        ),
    ]
