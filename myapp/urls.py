"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name ='myapp'



urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.indexview.as_view(),name='index'),
    path('tea/',views.tealist.as_view(), name='tea'),
    path('works/',views.lacelist.as_view(), name='lace'),
    path('create/', views.ContentCreate.as_view(), name='create'),
    path('myapp/detail/<int:pk>/', views.blogdetail.as_view(), name='blog_detail'),
    path('login/',views.Login.as_view(),name ='form')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
