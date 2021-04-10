from django.urls import path
from .api.views import HeadLinesListAPIView
from .views import LoginRegView, HomeView, user_profile, password_reset

app_name = 'portal'

urlpatterns = [
    path('api/news/', HeadLinesListAPIView.as_view(), name='head_lines'),
    path('', HomeView.as_view(), name='home'),
    path('profile/', user_profile, name='profile'),
    path('login/', LoginRegView.as_view(), name='login'),
    path('password-reset/', password_reset, name='password_reset')
]
