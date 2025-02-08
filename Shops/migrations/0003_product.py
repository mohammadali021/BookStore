# Generated by Django 5.1.6 on 2025-02-08 11:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shops', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام کتاب')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='قیمت')),
                ('discount_price', models.DecimalField(decimal_places=0, default='', max_digits=10, verbose_name='قیمت تخفیف خورده')),
                ('discount', models.BooleanField(default=False, verbose_name='تخفیف دارد؟')),
                ('description', models.TextField(default='', verbose_name='توضیح کوتاه در رابطه با محصول')),
                ('writer_name', models.CharField(default='', max_length=100, verbose_name='نام نویسنده')),
                ('translator', models.CharField(default='', max_length=100, verbose_name='نام مترجم')),
                ('new_book', models.BooleanField(default=False, verbose_name='کتاب جدید؟')),
                ('best_book', models.BooleanField(default=False, verbose_name='کتاب برجسته؟')),
                ('score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(6)])),
                ('Inventory', models.BooleanField(default=True)),
                ('count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shops.category', verbose_name='دسته بندی')),
            ],
        ),
    ]
