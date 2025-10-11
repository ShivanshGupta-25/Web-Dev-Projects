from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('post/<str:mypost>',views.post, name = 'post'),
    path('writeBlog',views.writeBlog, name = 'writeBlog')
]