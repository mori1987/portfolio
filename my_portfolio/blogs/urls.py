from django.urls import path
from . import views

app_name= 'blogs'

urlpatterns= [
    path('', views.BlogView.as_view(), name='blogs'),
    path('create/', views.CreatPostView.as_view(), name='create_post'),
    path('posts/', views.PostView.as_view(), name='posts'),
]