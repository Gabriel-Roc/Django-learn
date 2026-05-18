from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('lists/', views.view_list, name='lists'),
    path('lists/new/', views.new_list, name='new_list'),
]