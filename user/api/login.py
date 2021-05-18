from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class LoginSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': {
            'message': 'Login Fail',
        }
    }   
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        del data['refresh'] , data['access']
        data['message'] = 'Login successful'
        data['data'] = {}

        # Add extra responses here
        data['data']['username'] = self.user.username        

        data['data']['token'] = {}
        data['data']['token']['refresh'] = str(refresh)
        data['data']['token']['access'] = str(refresh.access_token)
        return data

class UserLogin(TokenObtainPairView):
    serializer_class = LoginSerializer


# {
#     "username" : "user1" ,
#     "password" : "123" 
# }


# {
#     "message": "Login successful",
#     "data": {
#         "username": "user1",
#         "token": {
#             "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMTQ0MDQ5MCwianRpIjoiYjc1Y2M0ODRkMmE5NDdiYzliNTFiOWYyNzRiOTBkNDIiLCJ1c2VyX2lkIjoxfQ.KIH26o9DnV2NAfnTMYJTyCy3vpWzyWLXjsOh9N_nufY",
#             "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxMzU3NjkwLCJqdGkiOiI4OGM4MzkxM2NkOWU0MmIwYTYxOWZiY2VjNGVlZTk4ZSIsInVzZXJfaWQiOjF9.Zmn5X-o82gXonHkkMT7EoBY8Ex5NQseePZpREsAd8xs"
#         }
#     }
# }