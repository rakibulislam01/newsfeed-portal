from django.urls import path

from .views import CreateUserView, CreateTokenView, UserProfileUpdateView, \
    LogoutAPIView, PasswordRestEmailAPIView

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('user-profile/', UserProfileUpdateView.as_view(), name='user_profile'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('password-reset/', PasswordRestEmailAPIView.as_view(), name='password-reset'),
    ]
