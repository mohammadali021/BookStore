# Generated by Django 5.1.5 on 2025-02-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shops', '0018_alter_product_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='token',
            field=models.CharField(blank=True, default='', max_length=6, null=True, unique=True),
        ),
    ]
