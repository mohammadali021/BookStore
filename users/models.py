from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class UserPannel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE  , related_name='pannel')
    phone_number = models.CharField(max_length=11, default='')
    wallet = models.DecimalField(max_digits=10, decimal_places=2 , default=0.00)
    address = models.TextField(null=True, blank=True, default='')
    image = models.ImageField(null=True, blank=True , upload_to='profile/', default='')
    slug = models.SlugField(default='', db_index=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user.username))
        super().save(*args, **kwargs)

