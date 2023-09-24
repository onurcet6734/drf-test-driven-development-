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
        fields = "__all__"

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
        customer_data = validated_data.pop('customer', [])
        if customer_data:
            customer, created = Customer.objects.get_or_create(**customer_data)
            instance.customer = customer

        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.order_date = validated_data.get('order_date', instance.order_date)

        # Updating manytomany menuitems
        if 'menuitem' in validated_data:
            menuitem_data = validated_data.pop('menuitem', [])

            # getting available menuitems
            current_menuitems = list(instance.menuitem.all())

            # Colleting all of menuitems
            updated_menuitems = []

            for item_data in menuitem_data:
                menuitem_id = item_data.get('id')

                # If menuitem_id is not present in the data or if existing menuitems do not have this ID, create a new menuitem
                if not menuitem_id or menuitem_id not in [item.id for item in current_menuitems]:
                    menuitem, created = MenuItem.objects.get_or_create(**item_data)
                else:
                    # If menuitem_id is available, use the menuitem with this ID
                    menuitem = MenuItem.objects.get(id=menuitem_id)

                updated_menuitems.append(menuitem)

            # Updating menuitems
            instance.menuitem.set(updated_menuitems)

        instance.save()
        return instance