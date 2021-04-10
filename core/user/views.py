from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import generics, authentication, permissions, status
from rest_framework import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings

from .models import Profile
from .serializers import UserSerializer, AuthTokenSerializer, UserProfileSerializer, \
    PasswordRestEmailSerializer
from .utils import Util


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for users"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    """"Manage the authenticated user"""
    serializer_class = UserProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        value = Profile.objects.get(user=self.request.user)
        return Response({
            "country_tag": value.country_tag,
            "source_tag": value.source_tag,
            "keyword_tag": value.keyword_tag
        })

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_object(self):
        return self.request.user


class LogoutAPIView(views.APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        try:
            self.request.auth.delete()
            message = 'Success'
            return Response(message, status.HTTP_204_NO_CONTENT)
        except:
            message = 'Invalid token.'
            return Response(message, status.HTTP_401_UNAUTHORIZED)


class PasswordRestEmailAPIView(generics.GenericAPIView):
    """Password reset request"""

    serializer_class = PasswordRestEmailSerializer

    def post(self, request):
        data = {'request': request, 'data': request.data}
        serializer = self.serializer_class(data=data)
        email = request.data['email']
        User = get_user_model()

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm',
                kwargs={'uidb64': uidb64, 'token': token})

            absurl = 'http://' + current_site + relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                         absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your password'}
            Util.send_email(data)
        return Response(
            {'Success': 'We have sent you a link to reset your password'},
            status=status.HTTP_200_OK)
