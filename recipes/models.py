from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    cooking_steps = models.TextField()
    ingredients = models.TextField()
    cooking_time = models.CharField(max_length=20)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('recipes_detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.title
