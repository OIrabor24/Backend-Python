from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from files.forms import UploadForm
from files.serializers import FileSerializer
from .models import File
from django.conf import settings

def index(request):
    return render(request, 'files/index.html')


def files(request): #list all
    data = File.objects.all()
    serializer = FileSerializer(data, many=True)
    return JsonResponse({'files': serializer.data}) 



# def file(request, file_id): # detail page
#     f = File.objects.get(pk=file_id) 
#     if f:
#         return render(request, 'files/file.html', {'file': f})  
#     else:
#         raise Http404('File does not exist.') 

# def edit(request, file_id):
#     name = request.POST.get('name') #attributes from our POST form!
#     file_type = request.POST.get('type')
#     f = File.objects.get(pk=file_id) 
#     print(name, file_type, f) 

#     if f:
#         if name: # if we get a file name input
#             f.name = name
#         if file_type: # if we get a file type input
#             f.file_type = file_type
#         f.save() # save post data
#         return redirect(files) # this redirects our POST request back to the files page
#     else: # This redirects us whether or not we receive user input data
#         return redirect(files) 

# def delete(request, file_id):
#     f = File.objects.get(pk=file_id) #delete a specific object
#     if f:
#         f.delete() # delete our object
#     return redirect(files) 

# def upload(request):
#     """We pass in AWS obj parameters bc we want to access the 
#     file name when we upload to our s3 bucket"""
#     form = UploadForm(request.POST, request.FILES) # 2 args( post and files, where files is where file is uploaded)
#     if form.is_valid(): #check if form is valid
#         settings.AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',
#         'ContentDisposition': 'attachment; filename="' + request.FILES['file'].name +'"'} # files comes from our model field file.
#         form.save() #save if valid 
#     return redirect(files) # redirect to a page