"""files URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views, settings
from django.conf.urls.static import static # allows us to serve static files
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    #CRUD Create, Read, Update, Delete
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #rest api urls
    path('api/files/', views.files, name='files'),
    path('api/file/<int:file_id>', views.file, name='file'), 
    path('api/register/', views.register, name='register'), 
    ]




    # path('files/', views.files, name='files'),
    # path('files/<int:file_id>/', views.file, name='file'),
    # path('files/edit/<int:file_id>/', views.edit, name='edit'),
    # path('files/delete/<int:file_id>/', views.delete, name='delete'),
    # path('files/upload', views.upload, name='upload')

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# allows us to serve static files