from django.urls import path
from . import views
import register.views as other_views

app_name = 'app_test'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('lists/', views.view_list, name='lists'),
    path('lists/new/', views.new_list, name='new_list'),
    path('logout/', other_views.logout, name='logout'),
    path('invalid_user/', views.invalid_user, name='invalid_user'),
]