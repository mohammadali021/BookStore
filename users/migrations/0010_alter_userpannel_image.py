# Generated by Django 5.1.6 on 2025-02-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_userpannel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpannel',
            name='image',
            field=models.ImageField(blank=True, default='aaaa.jpg', null=True, upload_to='profile/'),
        ),
    ]
