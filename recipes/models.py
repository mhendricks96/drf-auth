from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Recipe(models.Model):
  name = models.CharField(max_length=64)
  ingredients = models.TextField(max_length=600)
  description = models.TextField(max_length=600)
  added_at = models.DateField(auto_now_add=True)
  added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.name
