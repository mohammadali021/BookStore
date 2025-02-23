from django.db import models

# Create your models here.

class Users(models.Model):
    Name = models.CharField(max_length=50 ,verbose_name='نام')
    FamilyName = models.CharField(max_length=50 , verbose_name='نام خانوادگی')
    UserName = models.CharField(max_length=50 , verbose_name="نام کاربری")
    pass
