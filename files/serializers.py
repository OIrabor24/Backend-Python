#python object --> JSON
from rest_framework.serializers import ModelSerializer
from .models import File 

class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = '__all__' #you can provide fields in a list, but this syntax includes all fields
        