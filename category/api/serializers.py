from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

    def create(self, validated_data):
        """
        Create and return a new Category instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Category instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
