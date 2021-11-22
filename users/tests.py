import json
import bcrypt
import jwt

from django.test  import (
    Client,
    TransactionTestCase,
    TestCase
)
from django.conf  import settings

from users.models import User


class TestSignUpView(TransactionTestCase) :
    def setUp(self) :
        User.objects.create(
            id       = 1,
            username = 'test',
            password = bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        
    def tearDown(self) :
        User.objects.all().delete()
    
    def test_success_sign_up(self) :
        client = Client()
        
        user = {
            'id'       : 2,
            'username' : 'new user',
            'password' : '1234'
        }
        
        response = client.post("/users/signup", json.dumps(user), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': 'CREATE_USER'})
    
    def test_fail_sign_up_raise_key_error(self) :
        client = Client()
        
        user = {
            'id'       : 2,
            'ssername' : 'new user',
            'password' : '1234'
        }
        
        response = client.post("/users/signup", json.dumps(user), content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'KeyError'})
        
    def test_fail_sign_up_raise_integrity_error(self) :
        client = Client()
        
        user = {
            'id'       : 2,
            'username' : 'test',
            'password' : '1234'
        }
        
        response = client.post("/users/signup", json.dumps(user), content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'IntegrityError'})

class TestSignInView(TestCase) :
    def setUp(self) :
        user = User.objects.create(
            id       = 1,
            username = 'test',
            password = bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        
        global access_token
        access_token = jwt.encode({'username' : user.username}, settings.SECRET_KEY, settings.ALGORITHMS)
        
    def tearDown(self) :
        User.objects.all().delete()
    
    def test_success_sign_in(self) :
        client = Client()
        
        user = {
            'username' : 'test',
            'password' : '1234'
        }
        
        response = client.post('/users/signin', json.dumps(user), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'access_token': access_token})