# Generated by Django 5.1.4 on 2025-03-16 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_userprofilemodel_avg_performance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='avg_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
