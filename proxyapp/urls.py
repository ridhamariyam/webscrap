from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_proxy, name='proxy_list'),
]
