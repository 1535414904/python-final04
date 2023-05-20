"""
URL configuration for pythonfinal04 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
<<<<<<< HEAD
from mysite import views     # 從views.py去匯入所有的處理函式
urlpatterns = [
    path('admin/', admin.site.urls),
    path("filter/", views.filtered_data),
    path('', views.index),  # 如果有人來瀏覽首頁的話，請交給views.py裡面的index()函式處理
    path('kcg_data/', views.kcg_data)
=======
from mysite import views   # 從views.py去匯入所有的處理函式

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ), # 如果有人來瀏覽首頁的話，請交給views.py裡面的index()函式處理

>>>>>>> 0baf2dd9c19bbc4c0dc84da790a75aafe3bbdca5
]
