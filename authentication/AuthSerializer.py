from rest_framework import serializers


# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class AuthSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    device_id = serializers.CharField()


class VerifyOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    device_id = serializers.CharField()
    otp = serializers.IntegerField()


class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    device_id = serializers.CharField()
    otp = serializers.CharField(max_length=6)
    address = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
