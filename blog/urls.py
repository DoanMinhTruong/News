
from django.contrib import admin
from django.urls import path, include
from blog.api.create import Create
from blog.api.list import ListBlog
urlpatterns = [
    path('create/' , Create.as_view()  , name = 'create blog'),
    path('' , ListBlog.as_view() , name='list blog'),
    path('<int:pk>/' , ListBlog.as_view() , name='list blog'),
    # path('' , List.as_view() , name='list blog')

]
