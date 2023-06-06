from django.contrib import admin
from django.urls import path
from mysite import views     # 從views.py去匯入所有的處理函式
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("filter/", views.filtered_data),
    path('', views.index),  # 如果有人來瀏覽首頁的話，請交給views.py裡面的index()函式處理
    path('kcg_data/', views.kcg_data),
    path('all/', views.all)
]