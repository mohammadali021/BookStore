import secrets
import string

import shortuuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Model
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.apps import apps


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='دسته بندی کتاب ها')
    slug = models.SlugField(unique=True , db_index=True , null=True , allow_unicode=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(str(self.name))
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'نوع کتاب'
        verbose_name_plural = 'نوع دسته بندی کتاب'

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE , verbose_name='دسته بندی')
    name = models.CharField(max_length=100 , verbose_name='نام کتاب')
    price = models.DecimalField(max_digits=10 , decimal_places=0 , verbose_name='قیمت')
    discount_price = models.DecimalField(max_digits=10 , decimal_places=0, default='0', verbose_name='قیمت تخفیف خورده')
    discount = models.BooleanField(default=False ,verbose_name='تخفیف دارد؟')
    description = models.TextField(verbose_name='توضیح کوتاه در رابطه با محصول' ,default='')
    writer_name = models.CharField(max_length=100 , verbose_name='نام نویسنده',default='')
    translator = models.CharField(max_length=100 , verbose_name='نام مترجم',default='-')
    is_translator = models.BooleanField(default=False, verbose_name='مترجم دارد ؟')
    new_book = models.BooleanField(default=False ,verbose_name='کتاب جدید؟')
    best_book = models.BooleanField(default=False ,verbose_name='کتاب برجسته؟')
    score = models.IntegerField(default=0 , validators=(MaxValueValidator(6) , MinValueValidator(0)))
    unfill_score = models.IntegerField(default=0)
    Inventory = models.BooleanField(default=True  , verbose_name='موجودی')
    count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    slug = models.SlugField(db_index=True , null=True, blank=True)
    # token = models.CharField(max_length=6, blank=True,null=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        self.unfill_score = 6-self.score
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصول'

class Site_banner(models.Model):
    image = models.ImageField(upload_to='banners/', null=True, blank=True , verbose_name='تصویر کتب موجود در بنر')
    def __str__(self):
        return self.image.name
    class Meta:
        verbose_name = "تصاویر کتب بنر"
        verbose_name_plural = "تصاویر کتب بنر"
