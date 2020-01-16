# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView

from .AuthSerializer import AuthSerializer, VerifyOtpSerializer, RegisterSerializer
from .SMSSDK import SMS
from .models import User, UserDevice, OtpModel


class Auth(APIView):

    def post(self, request, format=None):
        '''
        Takes phone number and device_id from the serializer,
        If User is not found an otp is sent to the phone_number.
        If User is found: if the device is already registered then generate token
        and send otp if new device.
        :param request:
        :param format:
        :return:
        '''
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(phone_number=serializer.data['phone_number'])
                if user and user.is_active:
                    device_id = UserDevice.objects.get(user=user)
                    if serializer.data['device_id'] == device_id.device_id:
                        return JsonResponse({'status': "logged in",
                                             "user_exists": True,
                                             "token": user.get_token()},
                                            status=200)
                    else:
                        otp = SMS().send_otp(serializer.data['phone_number'])
                        return JsonResponse({'status': "OTP Sent.", "user_exists": True},
                                            status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                SMS().send_otp(serializer.data['phone_number'])
                return JsonResponse({'status': "OTP Sent.", "user_exists": False},
                                    status=200)
        else:
            return JsonResponse(serializer.error_messages)


class VerifyOtp(APIView):

    def post(self, request, format=None):
        '''
        Check if otp is valid, there is a user with existing then generate token.
        If there is  registered user, then generate token and register device.
        :param request:
        :param format:
        :return:
        '''
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            otp = OtpModel.objects.get(phone_number=serializer.data['phone_number'])
            if otp.is_valid(otp=serializer.data['otp']):
                user = User.objects.get(
                    phone_number=serializer.data['phone_number'])

                UserDevice.objects.create(user=user,
                                          device_id=serializer.data['device_id'])
                return JsonResponse(status=202,
                                    data={'status': 'logged in', 'key': user.get_token()})

            else:
                return JsonResponse({'error': 'Invalid OTP'}, status=401)
        else:
            return JsonResponse(serializer.error_messages)


class Register(APIView):
    def post(self, request):
        '''
        if the otp is valid and address is valid then crete new user and register the device.
        :param request:
        :return:
        '''
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            otp_in_db = get_object_or_404(OtpModel, phone_number=serializer.data['phone_number'])
            if int(serializer.data['otp']) == otp_in_db.otp:
                # todo verify address
                user = User.objects.create(phone_number=serializer.data['phone_number'])
                UserDevice.objects.create(user=user,
                                          device_id=serializer.data['device_id'])
                return JsonResponse(status=200, data={'status': 'ok',
                                                      'key': user.get_token()})
            else:
                return JsonResponse(status=400, data={'status': 'invalid otp'
                                                      })

        else:

            return JsonResponse(status=400, data={'error': serializer.error_messages})
