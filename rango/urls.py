from django.urls import path

from rango import views

app_name = 'rango'

urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('restricted/', views.restricted, name='restricted'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]

