from rest_framework import serializers
from ..models import Customer

class Customer_Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'email',
            'phone_number',
            'address',
            'national_id',
            'date_of_birth',
            'created_at',
            'updated_at'
        ]

        email = serializers.EmailField(required=False, allow_blank=True)
        phone_number = serializers.CharField(required=False)
        address = serializers.CharField(required=False)
        national_id = serializers.CharField(required=False)