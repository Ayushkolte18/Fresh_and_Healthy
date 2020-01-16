from rest_framework import serializers
from .models import User, CartItem

class CartSerializer(serializers.ModelSerializer):


    class Meta():
        model = CartItem
        fields = '__all__'

# class Cart(serializers.ModelSerializer):
#     user_auth = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
#
#     class Meta():
#         model = User
#         fields = '__all__'