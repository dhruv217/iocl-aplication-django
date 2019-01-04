from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    added_by = serializers.StringRelatedField(
        many=False,
        read_only=True
    )
    class Meta:
        model = Customer
        fields = ('id', 'url', 'name', 'address', 'photo_url',
                  'land_details', 'mobile_number', 'email', 'added_by')
