from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lists/', views.view_list, name='lists')
]