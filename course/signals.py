from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article

@receiver(post_save, sender = Article)
def article_saved(sender, instance, created, **kwargs):
    if created:
        print(f'New article created: {instance.title}')