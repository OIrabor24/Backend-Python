from django.http import Http404
from django.shortcuts import redirect, render
from .models import File

def index(request):
    return render(request, 'files/index.html')


def files(request): #list all
    data = File.objects.all()
    return render(request, 'files/files.html', {'files': data})

def file(request, file_id): # detail page
    f = File.objects.get(pk=file_id) 
    if f:
        return render(request, 'files/file.html', {'file': f})  
    else:
        raise Http404('File does not exist.') 

def edit(request, file_id):
    name = request.POST.get('name') #attributes from our POST form!
    file_type = request.POST.get('type')
    f = File.objects.get(pk=file_id) 
    print(name, file_type, f) 

    if f:
        if name: # if we get a file name input
            f.name = name
        if file_type: # if we get a file type input
            f.file_type = file_type
        f.save() # save post data
        return redirect(files) # this redirects our POST request back to the files page
    else: # This redirects us whether or not we receive user input data
        return redirect(files) 

def delete(request, file_id):
    f = File.objects.get(pk=file_id) #delete a specific object
    if f:
        f.delete() # delete our object
    return redirect(files) 