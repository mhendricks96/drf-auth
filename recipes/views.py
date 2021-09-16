from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# class RecipeList(generics.ListAPIView):
#   queryset = Recipe.objects.all()
#   serializer_class = RecipeSerializer

class RecipeList(generics.ListCreateAPIView):
  #permission_classes = (IsOwnerOrReadOnly,)
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer


# class RecipeDetail(generics.RetrieveAPIView):
#   queryset = Recipe.objects.all()
#   serializer_class = RecipeSerializer

# class RecipeDetail(generics.RetrieveUpdateAPIView):
#   queryset = Recipe.objects.all()
#   serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer

