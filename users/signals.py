from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from .utils import send_welcome_email



User = get_user_model()

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f'User {instance.username} created!')
        if instance.email:
            send_welcome_email(instance.email,instance.username)
