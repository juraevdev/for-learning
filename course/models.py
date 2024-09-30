from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

User = settings.AUTH_USER_MODEL

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    liked = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=True)
    notify_users_timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    active = models.BooleanField(default=True)

@receiver(post_save, sender = BlogPost)
def blog_post_post_save(sender, instance, created, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    