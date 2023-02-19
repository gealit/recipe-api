"""
Serializers for recipe APIs.
"""
from rest_framework.serializers import ModelSerializer

from core.models import Recipe


class RecipeSerializer(ModelSerializer):
    """Serializer for recipies."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']
