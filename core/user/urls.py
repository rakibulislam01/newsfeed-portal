from django.urls import path

from .views import CreateUserView, CreateTokenView, UserProfileUpdateView

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('user-profile/', UserProfileUpdateView.as_view(), name='user_profile'),
]
