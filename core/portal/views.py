from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'news/home.html'


class UserProfile(TemplateView):
    http_method_names = ['get', 'put']
    template_name = 'news/user_profile.html'


def user_profile(request):
    return render(request, 'news/user_profile.html')


class LoginRegView(TemplateView):
    template_name = 'news/login_reg_view.html'
