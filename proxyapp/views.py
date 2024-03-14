# views.py
from django.shortcuts import render
from django.http import HttpResponseServerError,HttpResponse
from .models import Proxy
import requests
from .tasks import scrape_proxy_list


def get_proxy(request):
    scrape_proxy_list.delay()
    proxies = Proxy.objects.all()
    
    return render(request, 'home.html', {'proxies': proxies})
    