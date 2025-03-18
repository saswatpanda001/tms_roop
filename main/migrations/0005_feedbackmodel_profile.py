# Generated by Django 5.1.4 on 2025-02-16 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_user_feedbackmodel_user_and_more'),
        ('users', '0010_alter_blogmodel_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmodel',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofilemodel'),
        ),
    ]
