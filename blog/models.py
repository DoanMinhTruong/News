from django.db import models
from new import settings
# Create your models here.

content_choices = [
    ("Tổng hợp" , 0),
    ("Xã hội" , 1) , 
    ("Thế giới" , 2) , 
    ("Kinh doanh" , 3),
    ("Công nghệ" , 4) ,
    ("Thể thao", 5), 
    ("Giải trí", 6),
]


class Blog(models.Model):
    title = models.CharField(max_length = 255, unique = True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_post_auth"
    )
    created_on      = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now = True)
    body = models.TextField()
    content = models.IntegerField(choices = content_choices , default=0)
    
