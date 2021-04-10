from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'news/home.html'


def user_profile(request):
    return render(request, 'news/user_profile.html')


class LoginRegView(TemplateView):
    template_name = 'news/login_reg_view.html'


def password_reset(request):
    return render(request, 'news/password_reset.html')
