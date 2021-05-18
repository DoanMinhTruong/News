from user.serializers import UserSerializers
from user.api.decode import decode_jwt
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
class UserUpdate(APIView):
    def put(self, request ,  *args, **kwargs):
        user = decode_jwt(request)
        if(user.username == request.data['username_now']):
            serializer = UserSerializers(user , data = request.data['update'] , partial = True)
            if serializer.is_valid():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                user_up = serializer.save()
                return JsonResponse({
                    "message" : "update successful"
                }, status = status.HTTP_200_OK)
            return JsonResponse({
                "message" : "update fail"
            },status = status.HTTP_400_BAD_REQUEST)
        return JsonResponse({
            "message" : "error"
        } , status = status.HTTP_400_BAD_REQUEST)


# {
#     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxMzU5Nzc1LCJqdGkiOiIzNjNkZmU2OTI1YjE0N2Q4OGM4OTkwOGZhYmE0MmE0ZCIsInVzZXJfaWQiOjV9.WmfLmjqYojsCl_wH3_Kmw3w85HmyQboJ8Az2JQP_0Us",
#     "username_now" : "user2" , 
#     "update" : {
#         "username" : "user2",
#         "password" : "1924",
#         "email" : "ok@gmail.com",
#     }
# }