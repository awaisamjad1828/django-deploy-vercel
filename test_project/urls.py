
from django.contrib import admin
from django.urls import path

from accounts.views import home,hello_world

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
