# Generated by Django 5.1.6 on 2025-02-24 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_userpannel_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpannel',
            name='image',
            field=models.ImageField(blank=True, default='profile/avatar.jpg', null=True, upload_to='profile/'),
        ),
    ]
