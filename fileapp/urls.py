from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('check-file/', views.check_file),
    path('open-file/', views.open_file),
    path('download-file/', views.download_file),
]
