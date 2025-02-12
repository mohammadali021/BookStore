import secrets
import string


from django.db import models
from django_quill.fields import QuillField



# Create your models here.
class SiteBlog(models.Model):
    title = models.CharField(max_length=100 , verbose_name='عنوان متن')
    content = QuillField(default='', verbose_name='ورود متن')
    slug3 = models.SlugField(unique=True , blank=True , null=True , max_length=6)
    token = models.CharField(max_length=6, unique=True, blank=True,null=True,default='')
    image = models.ImageField(upload_to='siteblog/', blank=True , null=True , default='')

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):


        self.token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))
        if not self.slug3:
            self.slug3 = (str(self.token))
        return super().save(*args , **kwargs)
    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ'
from django.db import models

# Create your models here.
