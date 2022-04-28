from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Author


@receiver(post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if created:
        print("-" * 100)
        print(instance)
        print(type(instance))
        print("-" * 100)
        Author.objects.get_or_create(user=instance)
    instance.author.save()
        # author.save()
    # instance.A.save()
        # new_author = Author(user=instance)
        # new_author.save()
