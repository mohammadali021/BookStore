# Generated by Django 5.1.5 on 2025-02-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shops', '0016_alter_product_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='token',
            field=models.CharField(blank=True, default='zf8T8T', max_length=6, null=True, unique=True),
        ),
    ]
