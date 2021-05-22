
from django.contrib import admin
from django.urls import path, include
from blog.api.create import Create
from blog.api.list import ListBlog
from blog.api.delete import DeleteBlog
urlpatterns = [
    path('create/' , Create.as_view()  , name = 'create blog'),
    path('' , ListBlog.as_view() , name='list blog'),
    path('<int:id>/' , ListBlog.as_view() , name='list blog'),
    path('<int:id>/delete' , DeleteBlog.as_view() , name='delete blog'),

]
