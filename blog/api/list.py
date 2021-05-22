from rest_framework.views import APIView
from blog.models import Blog
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from django.forms import model_to_dict
class ListBlog(APIView):
    def get(self, request , id = None):
        try:
            if(id):
                obj = Blog.objects.get(id = id)
                return JsonResponse(model_to_dict(obj))
            if(id == None):
                return JsonResponse(list(Blog.objects.all().values()), safe=False)
            return JsonResponse({
                    "message" :"dont have any blogs"
                },status = status.HTTP_204_NO_CONTENT)
        except:
            return JsonResponse({
                    "message" :"bad request"
                },status = status.HTTP_400_BAD_REQUEST)
            