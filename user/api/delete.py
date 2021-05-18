from user.api.decode import decode_jwt
from user.models import MyUser
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

class UserDelete(APIView):
    def delete(self, request):
        user = decode_jwt(request)
        if(user.is_admin):
            try:
                getuser = MyUser.objects.get(username = request.data['username'])
            except:
                return JsonResponse({
                    "message": "user not exists"
                }, status = status.HTTP_404_NOT_FOUND)
            getuser.delete()
            return JsonResponse({
                "message": "delete successfull"
            } , status = status.HTTP_200_OK)
        return JsonResponse({
            "message": "you dont have any permissions"
        }, status = status.HTTP_400_BAD_REQUEST)

# {
#     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxMzU3ODY3LCJqdGkiOiJkMGYzNzQ1NThkYWU0ODBjYjM4Y2QyMTAyYjJlMTI0NiIsInVzZXJfaWQiOjJ9.0ZKdaJVnzYcT7J0UTf-62Q7j_k8D04VSQZUHnIU5Nnw",
#     "username" : "user1"
# }