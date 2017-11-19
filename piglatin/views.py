from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    originalText= request.POST.get('text')
    return HttpResponse(originalText)