# Generated by Django 5.1.5 on 2025-02-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteblog', '0003_alter_siteblog_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteblog',
            name='slug3',
            field=models.SlugField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
