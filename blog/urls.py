from django.urls import path
from  . import views

app_name='blog'

urlpatterns = [

    path('',views.post_list,name='post_list'),
    path('add', views.add_Post, name='add_Post'),
    path('<str:slug>',views.post_detail,name='post_detail'),
    path('<str:slug>/edit',views.post_edit,name='post_edit'),
     path('delete/<str:slug>/',views.delete_List, name='delete_list'),


]