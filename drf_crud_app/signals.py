from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import NameDetails


@receiver(post_save, sender=NameDetails)
def notify_data_is_created(sender, instance, created, **kwargs):
    if created:
        print("\n\n")
        print("Data is created.")
        print("\n\n")
