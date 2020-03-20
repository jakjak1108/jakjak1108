from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('html/', views.html_response, name='html'),
    path('admin/', admin.site.urls),
]