"""
Serializers for recipe APIs.
"""
from rest_framework.serializers import ModelSerializer

from core.models import Recipe, Tag


class RecipeSerializer(ModelSerializer):
    """Serializer for recipies."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
