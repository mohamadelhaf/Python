from django.urls import URLPattern, path
from app_django import views

app_name = 'app_django'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.edit, name='edit'),
    path('', views.show, name='index')
]