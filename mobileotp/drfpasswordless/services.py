from django.utils.module_loading import import_string
from drfpasswordless.settings import api_settings
from drfpasswordless.utils import (
    create_callback_token_for_user,
)

# Messaging
from totp.smsmodule import SMS
import json

def send_otp(mobile, otp):
    message = "Your verification code is " + str(otp) + ". This code will expire in " + str(api_settings.PASSWORDLESS_TOKEN_EXPIRE_TIME) + " seconds"
    return SMS().send(mobile, message)

class TokenService(object):
    @staticmethod
    def send_token(user, alias_type, token_type, **message_payload):
        token = create_callback_token_for_user(user, alias_type, token_type)
        send_action = None

        if user.pk in api_settings.PASSWORDLESS_DEMO_USERS.keys():
            return True
        if alias_type == 'email':
            send_action = import_string(api_settings.PASSWORDLESS_EMAIL_CALLBACK)
        elif alias_type == 'mobile':
            send_action = import_string(api_settings.PASSWORDLESS_SMS_CALLBACK)
        # Send to alias
        success = send_action(user, token, **message_payload)
        return success


class SMSTokenService(object):
    @staticmethod
    def send_token(user, alias_type, token_type, **message_payload):
        token = create_callback_token_for_user(user, alias_type, token_type)
        send_action = None
        # Send to alias
        try:
            msg = send_otp(str(user), token)
            to_json = json.dumps(msg)
            as_json = json.loads(to_json)
            success = as_json['SMSMessageData']['Recipients'][0]['status']
        except Exception as e:
            success = str(e) 
        return success