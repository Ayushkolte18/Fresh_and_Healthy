import random
import urllib.parse
import urllib.request

from django.core.exceptions import ObjectDoesNotExist

from .models import OtpModel


class SMS:
    def __init__(self):
        self.key = ''
        self.error = ''

    def send_otp(self, phone_number):
        otp = random.randint(100000, 999999)
        msg = f'Your OTP for login is {otp}'
        if self.sendSMS(phone_number, '', msg):
            try:
                temp_otp = OtpModel.objects.get(phone_number=phone_number)
                temp_otp.otp = otp
                temp_otp.save()
            except ObjectDoesNotExist:
                OtpModel.objects.create(otp=otp,
                                        phone_number=phone_number,
                                        )

            return otp
        else:
            return self.error

    def sendSMS(self, numbers, sender, message):
        try:
            data = urllib.parse.urlencode({'apikey': self.key, 'numbers': numbers,
                                           'message': message, 'sender': sender})
            data = data.encode('utf-8')
            request = urllib.request.Request("https://api.textlocal.in/send/?")
            f = urllib.request.urlopen(request, data)
        except Exception as e:
            pass
