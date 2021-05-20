from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  
# Create your views here.

@csrf_exempt
def Hello(request):
    print('Hello!')
    response = HttpResponse("Hello!", content_type='text/plain')
    return response

