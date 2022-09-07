from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('post/<slug:pk>/', views.group_post),
]