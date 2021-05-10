from apps.dashboard.models import Asset
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        subject = f'Regarding Asset Added'
        message = f'Hi , New Asset Added to Techbox'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mdipakpatidar@gmail.com',]
        send_mail( subject, message, email_from, recipient_list,fail_silently=False,)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
		instance.profile.save()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)
