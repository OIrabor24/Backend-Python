from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello there')

data =  [
    {'name': 'image.jpg', 'type': 'jpg'},
    {'name': 'notes.txt', 'type': 'txt'},
    {'name': 'image2.jpg', 'type': 'jpg'}
    ] 

def files(request):
    print(data[0]) 
    return render(request, 'files/files.html', {'files': data})