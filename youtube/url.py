from django.urls import path
from . import views

app_name = 'youtube'
urlpatterns = [
    path('', views.index, name='index'),
    path('list_formats/', views.list_formats, name='list_formats'),
    path('download/<str:mime>/<int:filesize>/<str:title>/<path:url>', views.download, name='download'),
]
