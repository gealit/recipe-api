"""
URL mapping for the recipe app.
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe.views import (
    RecipeViewSet,
    TagViewSet,
    IngredientViewSet,
)


router = DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register('tags', TagViewSet, basename='tag')
router.register('ingredients', IngredientViewSet, basename='ingredient')

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
