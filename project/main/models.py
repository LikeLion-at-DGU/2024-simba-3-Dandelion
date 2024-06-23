from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.category

class Sutra(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50] + "..."

class Talisman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    talisman_category = models.CharField(max_length=10) # 법 구경 카테고리와는 다름!!
    text = models.TextField()
    discription = models.TextField()
    
