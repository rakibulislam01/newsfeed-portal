from django.contrib import admin
from django.urls import path
from .views import get_top_headlines

app_name = 'portal'

urlpatterns = [
    path('', get_top_headlines, name='headlines'),
]
