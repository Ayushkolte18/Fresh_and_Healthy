from django.db import models
from Product.models import Product
from django.contrib.auth.models import User
import datetime


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def cart_items(self):
        return CartItem.objects.filter(cart=self)

    @property
    def cart_sum(self):
        return sum([product.our_price for product in self.cart_items])



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta():
        db_table = 'cartitem'
