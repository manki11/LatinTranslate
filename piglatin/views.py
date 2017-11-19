from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    originalText= request.POST.get('text').lower()
    translation='';

    for word in originalText.split():
        if word[0] in ['a','e','i','o','u']:
            translation += word
            translation += 'way '
        else:
            translation+=word[1:]
            translation+=word[0]
            translation+='ay '


    return render(request, 'translate.html')