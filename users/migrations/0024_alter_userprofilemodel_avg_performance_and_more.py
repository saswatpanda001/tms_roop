# Generated by Django 5.1.4 on 2025-03-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_userprofilemodel_development_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='avg_performance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='avg_rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='avg_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
