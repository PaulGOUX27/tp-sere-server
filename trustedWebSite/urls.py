from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='index'),
    path('auth/', views.auth, name='auth'),
    path('connected/', views.connected, name='connected'),
    path('add/', views.add, name='add'),
]
