from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name']

    def create(self, validated_data):
        """
        Create and return a new Customer instance, given the validated data.
        """
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Customer instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
