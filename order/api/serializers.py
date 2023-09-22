from rest_framework import serializers
from order.models import Order
from customer.models import Customer
from menu.models import MenuItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price','category']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    menuitem = MenuItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['customer', 'menuitem', 'total_price', 'order_date']

    def create(self, validated_data):
        """
        Create and return a new Order instance, given the validated data.
        """
        customer_data = validated_data.pop('customer') 
        customer, created = Customer.objects.get_or_create(**customer_data) 

        menuitem_data = validated_data.pop('menuitem')
        menuitems = []
        for item_data in menuitem_data:
            menuitem, created = MenuItem.objects.get_or_create(**item_data)
            menuitems.append(menuitem)
        
        order = Order.objects.create(customer=customer, **validated_data)
        order.menuitem.set(menuitems) #set was used because of the many-to-many relationship

        return order

    def update(self, instance, validated_data):
        """
        Update and return an existing Order instance, given the validated data.
        """
        instance.customer = validated_data.get('customer', instance.customer)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.order_date = validated_data.get('order_date', instance.order_date)

        # Update the items in the order
        if 'menuitem' in validated_data:
            instance.menuitem.clear()
            for item_data in validated_data['menuitem']:
                item = MenuItem.objects.get(id=item_data['id'])
                instance.menuitem.add(item)

        instance.save()
        return instance
