from rest_framework import serializers
from Products.models import Orders

class OrderSerial(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'