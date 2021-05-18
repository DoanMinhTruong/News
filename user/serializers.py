from rest_framework import serializers
from .models import MyUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenVerifySerializer
from rest_framework_simplejwt.tokens import UntypedToken

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email' , 'username' , 'password']
        extra_kwargs = {'password': {'write_only': True}}