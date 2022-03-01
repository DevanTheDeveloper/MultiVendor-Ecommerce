from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,UserShipping

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs ):
        if created:
                Profile.objects.create(user=instance)
                UserShipping.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs ):
        instance.profile.save()
        pass

@receiver(post_save,sender=UserShipping)
def save_cxprofile(sender, instance, **kwargs ):
        instance.user.profile.save()
        pass