from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import UserPannel

@receiver(post_save, sender=User)
def create_user_pannel(sender, instance, created, **kwargs):
    if created:
        slug = slugify(instance.username)
        UserPannel.objects.create(user=instance, slug=slug)

