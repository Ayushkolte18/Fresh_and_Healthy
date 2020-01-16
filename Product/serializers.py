from rest_framework import serializers
from .models import Product, Category


# Create your...

class Prdouct_serializer(serializers.ModelSerializer):
    quantity = serializers.ModelSerializer

    class Meta():
        model = Product
        fields = '__all__'


class Category_serializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ['pk', 'title', "has_children"]
