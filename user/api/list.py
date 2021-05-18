from .decode import decode_jwt
from user.models import MyUser
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
class ListUser(APIView):
    def post(self, request):
        try:
            user = decode_jwt(request)
            if user.is_admin:
                list_user = MyUser.objects.all()
                if not list_user:
                    return JsonResponse({
                        "message" : "dont have any user"
                    },status = status.HTTP_204_NO_CONTENT)
                return JsonResponse(list(MyUser.objects.all().values()), safe=False)
            return JsonResponse({
                "message": "not admin"
            } , status = status.HTTP_401_UNAUTHORIZED)
        except:
            return JsonResponse({
                "message": "error"
            }, status = status.HTTP_401_UNAUTHORIZED)