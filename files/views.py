from functools import partial
from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from files.forms import UploadForm
from files.serializers import FileSerializer
from .models import File
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view, permission_classes #api permissions
from rest_framework.permissions import IsAuthenticated #forces login to access api endpoint

def index(request):
    return render(request, 'files/index.html')

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def files(request): #list all #get=search put=update, post=save to db, delete=delete
    if request.method == 'GET':
        data = File.objects.all()
        serializer = FileSerializer(data, many=True)
        return Response({'files': serializer.data}) 
    
    elif request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def file(request, file_id):
    try:
        data = File.objects.get(pk=file_id)
    except File.DoesNotExist: #return error
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FileSerializer(data) 
        return Response({'file': serializer.data}) 

    elif request.method == 'PATCH':
        serializer =FileSerializer(data, data=request.data, partial=True) #2nd arg is the data that is changed/updated to the db
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

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