from new import settings
from user.models import MyUser
import jwt

def decode_jwt(request):
    class Temp:
        def __init__(self, is_admin):
            self.is_admin = is_admin
    try:
        data = jwt.decode(request.data['token'], settings.SECRET_KEY,  algorithms=['HS256'])
        user_id = data["user_id"]
        user = MyUser.objects.get(pk = user_id)
        return user
    except:
        # user = MyUser.objects.create(username = 'temp' , email = 'temp@gmail.com' ,is_admin = False)
        user = Temp(is_admin= False)
        return user