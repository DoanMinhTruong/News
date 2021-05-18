
from django.contrib import admin
from django.urls import path, include
from .api.register import UserRegister
from .api.login import UserLogin
from .api.list import ListUser
from .api.delete import UserDelete
from .api.update import UserUpdate
urlpatterns = [
    path('register/' , UserRegister.as_view() , name='user register'),
    path('login/' , UserLogin.as_view() , name='user login'),
    path('delete/' , UserDelete.as_view() , name='user delete'),
    path('update/' , UserUpdate.as_view() , name='user update'),
    path('' , ListUser.as_view() , name='user list'),
]
