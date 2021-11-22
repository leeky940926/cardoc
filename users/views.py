import bcrypt
import json
import jwt

from django.http     import JsonResponse
from django.views    import View
from django.db.utils import IntegrityError

from users.models    import User
from cardoc.settings import (
    ALGORITHMS,
    SECRET_KEY
)

class SignUpView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)
        
            username = data['username']            
            password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            User.objects.create(username = username, password = password)
            
            return JsonResponse({'message' : 'CREATE_USER'}, status=201)
        
        except KeyError :
            return JsonResponse({'message' : 'KeyError'}, status=400)

        except IntegrityError :
            return JsonResponse({'message' : 'IntegrityError'}, status=400)
        
class SignInView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)
      
            user = User.objects.get(username = data['username'])
            
            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) :
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=400)
        
            access_token = jwt.encode({'username':user.username}, SECRET_KEY, ALGORITHMS)
            
            return JsonResponse({'access_token' : access_token}, status=200)
        
        except KeyError :
            return JsonResponse({'message' : 'KeyError'}, status=400)

        except User.DoesNotExist :
            return JsonResponse({'message' : 'User.DoesNotExist'}, status=400)