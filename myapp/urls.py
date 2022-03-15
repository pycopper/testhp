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
from . import views

app_name ='myapp'



urlpatterns = [
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('contact.html',views.contact,name='contact'),
    path('recruit.html',views.recruit,name='recruit'),
    path('sitemap.html',views.sitemap,name='sitemap'),
    path('menu.html',views.menu,name='menu'),
    path('works.html',views.works,name='works'),
    path('staff.html',views.staff,name='staff'),
    path('shop.html',views.shop,name='shop'),
    path('access.html',views.access,name='access'),
    path('link.html',views.link,name='link'),
]
