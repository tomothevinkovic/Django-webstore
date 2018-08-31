from django.contrib import admin
from django.urls import path
from . import views, models

app_name = 'items'

urlpatterns = [
    path('', views.index, name = 'index'),

    path('login_signup/', views.login, name = 'login'),

    path('users/<str:username>/', views.userprofile, name = 'userprofile'),

    path('my_profile/', views.my_profile, name = 'index'),

    path('register/', views.login, name = 'register'),

    path('logout/', views.logout, name = 'logout'),

    path('add_a_product/', views.add_a_product, name = 'add_a_product'),

    path('<str:category_name>/', views.subs, name = 'subs'),

    path('<str:category_name>/<str:sub_name>/', views.products, name = 'products'),

    path('<str:category_name>/<str:sub_name>/<str:product_name>/', views.product_detail, name = 'product_detail'), 


]
