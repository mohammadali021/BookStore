import secrets
import string


from django.db import models
from django_quill.fields import QuillField
from django.apps import apps




# Create your models here.
class SiteBlog(models.Model):

    title = models.CharField(max_length=100 , verbose_name='عنوان متن')
    content = QuillField(default='', verbose_name='ورود متن')
    slug3 = models.SlugField( blank=True , null=True , max_length=6)
    token = models.CharField(max_length=6, blank=True,null=True , default='')
    image = models.ImageField(upload_to='siteblog/', blank=True , null=True)


    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug3:
            self.slug3 = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
            while Product.objects.filter(slug=self.slug3).exists():
                self.slug3 = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        return super().save(*args , **kwargs)
    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ'

# Create your models here.
