from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


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
    Inventory = models.BooleanField(default=True  , verbose_name='موجودی')
    count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    slug = models.SlugField(unique=True , db_index=True , null=True, blank=True , allow_unicode=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{str(self.name)}-{str(self.price)}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصول'




