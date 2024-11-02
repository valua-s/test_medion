from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Employee, User


@receiver(pre_save, sender=User)
def set_activation_date(sender, instance, **kwargs):
    if instance.role == 'admin':
        instance.is_stuff = True


@receiver(pre_save, sender=Employee)
def pre_save(sender, instance, **kwargs):
    if instance.is_fired is False:
        instance.fire_date = None
