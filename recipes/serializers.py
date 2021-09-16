from rest_framework import serializers
from.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'ingredients', 'description', 'added_by')
    model = Recipe