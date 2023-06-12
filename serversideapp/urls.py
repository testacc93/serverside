from django.contrib import admin
from django.urls import path, include
from . import views
from serverside import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
] + static(settings.STATIC_URL)
