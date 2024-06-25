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
    like_count = models.IntegerField(default=0)
    num108_count = models.IntegerField(default=0)

    
class SharedWish(models.Model):
    title = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='sharedwish_likes', blank=True)
    like_count = models.IntegerField(default=0)
    num108_count = models.IntegerField(default=0)

    def summary(self):
        return self.title[:7] + "..."