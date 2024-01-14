from rest_framework import serializers
from .models import Customer, Pharmacy, Medicines, Purchasing, Sales, Reports

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    branch = CustomerSerializer()

    class Meta:
        model = Pharmacy
        fields = '__all__'

class MedicinesSerializer(serializers.ModelSerializer):
    branch = CustomerSerializer()

    class Meta:
        model = Medicines
        fields = '__all__'

class PurchasingSerializer(serializers.ModelSerializer):
    branch = CustomerSerializer()

    class Meta:
        model = Purchasing
        fields = '__all__'


class saleSerializer(serializers.ModelSerializer):
    branch = CustomerSerializer()

    class Meta:
        model = Sales
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    branch = CustomerSerializer()

    class Meta:
        model = Reports
        fields = '__all__'


