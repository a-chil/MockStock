from django.db.models.signals import post_save
from django.contrib.auth.models import User
from main.models import Profile


def profile_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
        )
        print("Profile created")


post_save.connect(profile_create, sender=User)
