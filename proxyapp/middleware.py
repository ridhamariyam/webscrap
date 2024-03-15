from django.http import HttpResponse
from django.conf import settings

class ChromeUserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        if 'Chrome' in user_agent:
            return HttpResponse(status=499) 
        
        return self.get_response(request)