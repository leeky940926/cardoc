import json
import jwt
import bcrypt
from django.http import response

from django.test  import (
    TestCase,
    Client
)
from users.models import User
from trims.models import (
    Brand,
    ModelGroup,
    SubModel,
    SubModelGroup,
    AvailableYearType,
    Grade,
    Trim,
    FrontTire,
    RearTire,
    TrimUser
)
from django.conf import settings

class TestTrimView(TestCase) :
    def setUp(self) :
        global user1, brand1, trim1, front1, rear1, modelgroup1, submodel1, yearType1, submodel1, grade1, headers1
        
        user1          = User.objects.create(id=1, username='test', password=bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'))
        brand1         = Brand.objects.create(id=1, brandName='기아test', brandNameEng='Kiatest', country='KORtest', brandImageUrl="test_url", brandUrl="test_url")
        modelgroup1    = ModelGroup.objects.create(id=1, modelName = "오피러스test", brand = brand1)
        submodelGroup1 = SubModelGroup.objects.create(id=1, submodelGroupYearTypeFrom = 2003, submodelGroupYearTypeTo = 2006, submodelGroupName='오피러스test', modelGroup = modelgroup1)
        yearType1      = AvailableYearType.objects.create(id=1, yearType = 2004)
        submodel1      = SubModel.objects.create(id=1, submodelName = '오피러스test', submodelNameEng = '오피러스test', yearType = yearType1, submodelImageUrl="url_test", submodelGroup=submodelGroup1)
        grade1         = Grade.objects.create(id=1, gradeName="2.7 가솔린test", fuelType='Gasolinetest', displacement=2656, submodel = submodel1)
        trim1          = Trim.objects.create(id=1, trimName='GH270 고급형', salesCode=3, bodySize='E', bodyStyle='SEDAN', transmission="A/T", price=30050000, priceUnit=0, isRecommended=False, releaseDate='2004-01-01', discontinuedDate='2006-06-01', carTypeCode=1, grade=grade1)
        front1         = FrontTire.objects.create(id=1, name='타이어 전', value="225/60R16", unit='', multiValues='', trim = trim1)
        rear1          = RearTire.objects.create(id=1, name='타이어 후', value="225/60R16", unit='', multiValues='', trim = trim1)
        trim_users     = TrimUser.objects.create(id=1, user=user1, trim=trim1)
        headers1        = {'HTTP_Authorization' : jwt.encode({'username' : user1.username}, settings.SECRET_KEY, settings.ALGORITHMS)}
    
    def tearDown(self) :
        User.objects.all().delete()
        Brand.objects.all().delete()
        ModelGroup.objects.all().delete()
        SubModelGroup.objects.all().delete()
        AvailableYearType.objects.all().delete()
        SubModel.objects.all().delete()
        Grade.objects.all().delete()
        Trim.objects.all().delete()
        FrontTire.objects.all().delete()
        RearTire.objects.all().delete()
    
    def test_success_post_trim(self) :
        client = Client()
        
        data = [{
            'id'     : 'test',
            'trimId' : 1
        }]
        
        response = client.post('/trims', json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'message' : 'TRIM_CREATE'
        })
    
    def test_failure_post_raise_key_error(self) :
        client = Client()
        
        data = [{
            'ids'    : 'test',
            'trimId' : 1
        }]
        
        response = client.post('/trims', json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'KeyError'
        })
    
    def test_failure_post_raise_trim_does_not_exist(self) :
        client = Client()
        
        data = [{
            'id'     : 'test',
            'trimId' : 100
        }]
        
        response = client.post('/trims', json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'Trim.DoesNotExist'
        })
    
    def test_failure_post_raise_user_does_not_exist(self) :
        client = Client()
        
        data = [{
            'id'     : 'testsssss',
            'trimId' : 1
        }]
        
        response = client.post('/trims', json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'User.DoesNotExist'
        })
    
    def test_success_get_trims(self) :
        client = Client()
        
        response = client.get('/trims', **headers1)
        
        data = [{
            'id'         : 'test',
            'front_tire' : [{
                'name'        : '타이어 전', 
                'value'       : "225/60R16",
                'unit'        : '',
                'multiValues' : ''
            }],
            'rear_tire' : [{
                'name'        : '타이어 후',
                'value'       : '225/60R16',
                'unit'        : '',
                'multiValues' : ''
            }]
        }]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            'data' : data
        })
    

class TestTrimPathView(TestCase) :
    def setUp(self) :
        global user1, brand1, trim1, front1, rear1, modelgroup1, submodel1, yearType1, submodel1, grade1
        
        user1          = User.objects.create(id=1, username='test', password=bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'))
        brand1         = Brand.objects.create(id=1, brandName='기아test', brandNameEng='Kiatest', country='KORtest', brandImageUrl="test_url", brandUrl="test_url")
        modelgroup1    = ModelGroup.objects.create(id=1, modelName = "오피러스test", brand = brand1)
        submodelGroup1 = SubModelGroup.objects.create(id=1, submodelGroupYearTypeFrom = 2003, submodelGroupYearTypeTo = 2006, submodelGroupName='오피러스test', modelGroup = modelgroup1)
        yearType1      = AvailableYearType.objects.create(id=1, yearType = 2004)
        submodel1      = SubModel.objects.create(id=1, submodelName = '오피러스test', submodelNameEng = '오피러스test', yearType = yearType1, submodelImageUrl="url_test", submodelGroup=submodelGroup1)
        grade1         = Grade.objects.create(id=1, gradeName="2.7 가솔린test", fuelType='Gasolinetest', displacement=2656, submodel = submodel1)
        trim1          = Trim.objects.create(id=1, trimName='GH270 고급형', salesCode=3, bodySize='E', bodyStyle='SEDAN', transmission="A/T", price=30050000, priceUnit=0, isRecommended=False, releaseDate='2004-01-01', discontinuedDate='2006-06-01', carTypeCode=1, grade=grade1)
        front1         = FrontTire.objects.create(id=1, name='타이어 전', value="225/60R16", unit='', multiValues='', trim = trim1)
        rear1          = RearTire.objects.create(id=1, name='타이어 후', value="225/60R16", unit='', multiValues='', trim = trim1)
    
    def tearDown(self) :
        User.objects.all().delete()
        Brand.objects.all().delete()
        ModelGroup.objects.all().delete()
        SubModelGroup.objects.all().delete()
        AvailableYearType.objects.all().delete()
        SubModel.objects.all().delete()
        Grade.objects.all().delete()
        Trim.objects.all().delete()
        FrontTire.objects.all().delete()
        RearTire.objects.all().delete()
        
    def test_success_get_trim(self) :
        client = Client()
        
        data = {
            'brandId'                   : brand1.id,
            'brandName'                 : brand1.brandName,
            'brandNameEng'              : brand1.brandNameEng,
            'country'                   : brand1.country,
            'isImported'                : brand1.imImported,
            'brandImageUrl'             : brand1.brandImageUrl,
            'brandUrl'                  : brand1.brandUrl,
            'modelId'                   : 1,
            'modelName'                 : '오피러스test',
            'submodelGroupId'           : 1, 
            'submodelGroupYearTypeFrom' : 2003,
            'submodelGroupYearTypeTo'   : 2006,
            'submodelGroupName'         : '오피러스test',
            'submodelId'                : 1,
            'submodelName'              : '오피러스test',
            'yearType'                  : 2004,
            'submodelImageUrl'          : 'url_test',
            'gradeId'                   : trim1.grade.id,
            'gradeName'                 : trim1.grade.gradeName,
            'fuelType'                  : trim1.grade.fuelType,
            'displacement'              : trim1.grade.displacement,
            'trimId'                    : trim1.id,
            'trimName'                  : trim1.trimName,
            'salesCode'                 : trim1.salesCode,
            'bodySize'                  : trim1.bodySize,
            'bodyStyle'                 : trim1.bodyStyle,
            'transmission'              : trim1.transmission,
            'price'                     : trim1.price,
            'priceUnit'                 : trim1.priceUnit,
            'isRecommended'             : trim1.isRecommended,
            'releaseDate'               : trim1.releaseDate,
            'discontinuedDate'          : trim1.discontinuedDate,
            'carTypeCode'               : trim1.carTypeCode,
            'spec' : {
                'front_tire' : [{
                    'name'        : front.name,
                    'value'       : front.value,
                    'unit'        : front.unit,
                    'multiValues' : front.multiValues
                } for front in trim1.fronttire_set.all()],
                'rear_tire' : [{
                    'name'        : rear.name,
                    'value'       : rear.value,
                    'unit'        : rear.unit,
                    'multiValues' : rear.multiValues
                } for rear in trim1.reartire_set.all()],
            }
        }
        
        response = client.get('/trims/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            'message' : data
        })
    
    def test_failure_trim_does_not_exist(self) :
        client = Client()
      
        response = client.get('/trims/100')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{
            'message' : 'Trim.DoesNotExist'
        })