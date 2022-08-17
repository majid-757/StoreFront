from django.urls import path

from .views import say_hello


app_name = 'playground'

urlpatterns = [
    path('hello/', say_hello),
]










