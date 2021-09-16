from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Recipe

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_recipe = Recipe.objects.create(
            added_by = testuser1,
            name = 'taco',
            ingredients = 'stuff',
            description = 'great',
            added_at = '1987-12-03'
        )
        test_recipe.save()

    def test_recipe_content(self):
        recipe = Recipe.objects.get(id=1)
        actual_administator = str(recipe.added_by)
        actual_name = str(recipe.name)
        actual_ingredients = str(recipe.ingredients)
        self.assertEqual(actual_administator, 'testuser1')
        self.assertEqual(actual_name, 'taco')
        self.assertEqual(actual_ingredients, 'stuff')

# Create your tests here.
