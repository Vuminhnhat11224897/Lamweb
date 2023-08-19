from django.urls import path
from . import views

urlpatterns = [
    path('', views.index23, name = 'index'),
]
