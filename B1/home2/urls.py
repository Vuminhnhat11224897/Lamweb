from django.urls import path
from . import views

urlpatterns = [
    path('', views.index123, name = 'index'),
]