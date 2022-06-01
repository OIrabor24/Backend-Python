from django.http import Http404
from django.shortcuts import render

def index(request):
    return render(request, 'files/index.html')

data =  [
    {'id': 0, 'name': 'image.jpg', 'type': 'jpg'},
    {'id': 1, 'name': 'notes.txt', 'type': 'txt'},
    {'id': 2, 'name': 'image2.jpg', 'type': 'jpg'}
    ] 


def files(request): #list all
    return render(request, 'files/files.html', {'files': data})

def file(request, file_id): # detail page
    print('File ID:', file_id)  
    f = next((item for item in data if item.get('id')== file_id), None) 
    if f:
        return render(request, 'files/file.html', {'file': f})  
    else:
        raise Http404('File does not exist.') 