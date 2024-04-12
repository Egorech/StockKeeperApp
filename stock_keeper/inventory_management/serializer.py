from rest_framework import serializers
from .models import Shelf

class ShelfSerializer(serializers.ModelSerializer):
    shelf_id = serializers.IntegerField(source='id')
    location_name = serializers.CharField(source='location.name')
    product_name = serializers.CharField(source='product.name')

    class Meta:
        model = Shelf
        fields = ['shelf_id', 'location_name', 'product_name', 'current_quantity']