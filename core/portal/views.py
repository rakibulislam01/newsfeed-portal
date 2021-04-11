from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """User home view"""
    template_name = 'news/home.html'


def user_profile(request):
    """User profile"""
    return render(request, 'news/user_profile.html')


class LoginRegView(TemplateView):
    """User login view"""
    template_name = 'news/login_reg_view.html'


def password_reset(request):
    """user password reset"""
    return render(request, 'news/password_reset.html')
