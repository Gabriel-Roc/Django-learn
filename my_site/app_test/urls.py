from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view1/', views.view1, name='view1'),
]