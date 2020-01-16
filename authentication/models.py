# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token


class Address(models.Model):
    pass


class User(AbstractUser):
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)

    def get_token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token.key

    def supersave(self, *args, **kwargs):
        self.username = self.phone_number
        self.supersave()


class OtpModel(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.IntegerField()
    created_time = models.DateTimeField(auto_now=True)

    def is_valid(self, otp):
        if (timezone.now() - self.created_time).seconds < 900 and int(otp) == int(self.otp):
            self.delete()
            return True
        else:
            self.delete()
            return False


class UserDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=30)
