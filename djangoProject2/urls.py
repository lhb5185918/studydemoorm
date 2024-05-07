"""
URL configuration for djangoProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,re_path
from booktest import views
from ajaxApp import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.add),
    path('index/',views.index),
    path('addbook/',views.addbook),
    re_path('deletebook/(\d+)',views.deletebook),
    re_path('editpage/(\d+)',views.editpage),
    path('register/',v2.register),
    path("ajax_register/",v2.ajax_register),

]
