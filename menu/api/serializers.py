from rest_framework import serializers
from menu.models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category']

    def create(self, validated_data):
        """
        Create and return a new MenuItem instance, given the validated data.
        """
        return MenuItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing MenuItem instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
