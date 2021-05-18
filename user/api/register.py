from django.http import JsonResponse
from user.serializers import UserSerializers
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.views import APIView
class UserRegister(APIView):
    def post(self, request):
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            return JsonResponse(
                {'message': 'Register Successfull!'}
            , status = status.HTTP_201_CREATED)
        return JsonResponse({
            'message': 'Register Fail !'
            }, status = status.HTTP_400_BAD_REQUEST)


# {
#     "email" : "user1@gmail.com",
#     "username" : "user1" , 
#     "password" : "123" 
# }