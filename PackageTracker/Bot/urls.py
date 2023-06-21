from django.contrib import admin
from django.urls import path
from Bot.views import home
from Bot import views
urlpatterns = [
    path('5761837078:AAE8swqpRKGalpjwOaM4RKZXtDHIWn3-654', home),
    path('set_webhook/', views.set_webhook)  
]
