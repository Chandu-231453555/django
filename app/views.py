from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def unique(request):
    return HttpResponse('Unqiue King')

def chandu(request):
    return HttpResponse('<h1>FREE FIRE KING  OF BC HOSTELL</h1>')

def chandu1(request):
    return HttpResponse('<h1><marquie>First Crush</marquie></h1>')

def chandu2(request):
    return HttpResponse('''
                            <h1>First Love </h1>
                         <img src='C:\Users\chandu\Desktop\WEBPAGE\WhatsApp Image 2023-12-17 at 21.55.54_9b8006a6.jpg'>
                        ''')
def chandu3(request):
    return HttpResponse('Focouse on feature')

def python(request):
    return HttpResponse('Learning python')

def after(request):
    return HttpResponse('waiting........')