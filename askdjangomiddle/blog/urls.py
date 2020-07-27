from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_List, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]