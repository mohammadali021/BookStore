# Generated by Django 5.1.5 on 2025-02-13 07:43

import siteblog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteblog', '0006_alter_siteblog_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteblog',
            name='token',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
