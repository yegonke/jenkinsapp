from drfpasswordless.settings import api_settings
from django.urls import path
from drfpasswordless.views import (
     ObtainMobileCallbackToken,
     ObtainAuthTokenFromCallbackToken,
)


from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  # <-- Here

app_name = 'drfpasswordless'

#Test token authentication

class TestView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here
    authentication_classes = [TokenAuthentication,]
    @staticmethod
    def get(request):
         return Response({"otp": "You are seeing this site as "+ str(request.user) + " using a token"}, status=200)  # Just for demonstration


urlpatterns = [
     path(api_settings.PASSWORDLESS_AUTH_PREFIX + "test/", TestView.as_view(), name="Test"),
     path(api_settings.PASSWORDLESS_AUTH_PREFIX + 'mobile/', ObtainMobileCallbackToken.as_view(), name='auth_mobile'),
     path(api_settings.PASSWORDLESS_AUTH_PREFIX + 'token/', ObtainAuthTokenFromCallbackToken.as_view(), name='auth_token'),
]
