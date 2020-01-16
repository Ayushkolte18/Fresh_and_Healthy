from django.contrib import admin
from .models import CartItem, Cart,User
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(User)