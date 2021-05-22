from blog.models import Blog
from rest_framework.views import APIView
from blog.api.decode import decode_jwt
from django.http import JsonResponse
from rest_framework import status
from blog.serializers import BlogSerializer
class Create(APIView):
    def post(self, request):
        user = decode_jwt(request)
        if(user.is_active):
            datum = request.data['blog']
            datum['author'] = user.pk
            serializer = BlogSerializer(data = datum)
            if(serializer.is_valid()):
                serializer.save()
                return JsonResponse({
                    "message" : "ok"
                } , status = status.HTTP_200_OK)
            return JsonResponse({
                "message" : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({
                "message" : "token not exist"
            } , status = status.HTTP_400_BAD_REQUEST)
