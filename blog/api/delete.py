from rest_framework.views import APIView
from blog.models import Blog
from rest_framework import status
from django.http import JsonResponse
from blog.api.decode import decode_jwt

class DeleteBlog(APIView):
    def post(self, request, id):
        user = decode_jwt(request)
        if(user.is_active):
            try:
                if(user.is_admin):
                    blog = Blog.objects.get(id = id)
                else:
                    blog = Blog.objects.get(id = id , author_id = user.id)
                if(blog):
                    blog.delete()
                    return JsonResponse({
                        "message" : "delete successfully"
                    }, status = status.HTTP_200_OK)
                return JsonResponse({
                    "message" : "blog not exist"
                }, status = status.HTTP_204_NO_CONTENT)
            except:
                return JsonResponse({
                    "message" : "something went wrong"
                } , status = status.HTTP_400_BAD_REQUEST)
