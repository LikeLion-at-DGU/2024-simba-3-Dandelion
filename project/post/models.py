from django.db import models
from django.contrib.auth.models import User
from main.models import Category
# Create your models here.
class Past(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    my_sutra = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Future(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    my_sutra = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class MyWish(models.Model):
    title = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.IntegerField(default=0)
    num108_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.text[:50] + "..."
class SharedWish(models.Model):
    wish = models.ForeignKey(MyWish, on_delete=models.CASCADE, related_name='my_wish')