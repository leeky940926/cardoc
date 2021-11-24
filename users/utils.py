import jwt

from django.http     import JsonResponse

from cardoc.settings import (
    ALGORITHMS,
    SECRET_KEY
)
from users.models    import User

def login_required(func) :
    def wrapper(self, request, *args, **kwargs) :
        try :
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, SECRET_KEY, ALGORITHMS)
            user         = User.objects.get(username = payload['username'])
            request.user = user
            
        except jwt.exceptions.DecodeError :
            return JsonResponse({'message' : 'DecodeError'}, status=401)
        
        except User.DoesNotExist :
            return JsonResponse({'message' : 'DoesNotExist'}, status=401)
        
        return func(self, request, *args, **kwargs)
    
    return wrapper