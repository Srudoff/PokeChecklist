from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from checklist.models import Card


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = ImageField(upload_to='profiles')
    checklist = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a new Django User is created"""
    if created:
        Profile.objects.create(user=instance)
        Card.objects.create(checklist=instance)