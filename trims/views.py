import json

from django.db    import transaction
from django.views import View
from django.http  import JsonResponse

from users.models import User
from users.utils  import login_required
from trims.models import (
    Brand,
    ModelGroup,
    SubModel,
    SubModelGroup,
    Trim,
    TrimUser
)

class TrimView(View) :
    def post(self, request) :
        try :
            with transaction.atomic() :
                data = json.loads(request.body)
                
                if len(data) >5 :
                    return JsonResponse({'message' : 'TOO_MUCH_LIST'}, status=400)
                
                for datum in data :
                    
                    user = User.objects.get(username = datum['id'])
                    trim = Trim.objects.get(id = datum['trimId'])
                    
                    TrimUser.objects.create(user = user, trim = trim)
            
            return JsonResponse({'message' : 'TRIM_CREATE'}, status=201)
            
        except KeyError :
            return JsonResponse({'message' : 'KeyError'}, status=400)
        
        except AttributeError :
            return JsonResponse({'message' : 'AttributeError'}, status=400)

        except Trim.DoesNotExist :
            return JsonResponse({'message' : 'Trim.DoesNotExist'}, status=400)

        except User.DoesNotExist :
            return JsonResponse({'message' : 'User.DoesNotExist'}, status=400)
    
    @login_required
    def get(self, request) :
        try : 
            trim_id_list = list(set([trim.trim_id for trim in TrimUser.objects.filter(user = request.user)]))
        
            trims = Trim.objects.prefetch_related('fronttire_set', 'reartire_set').filter(id__in = trim_id_list)
            
            data = [
                {
                'id'         : request.user.username,
                'front_tire' : [{
                        'name'        : front.name,
                        'value'       : front.value,
                        'unit'        : front.unit,
                        'multiValues' : front.multiValues
                    } for front in trim.fronttire_set.all()],
                'rear_tire' : [{
                    'name'        : rear.name,
                    'value'       : rear.value,
                    'unit'        : rear.unit,
                    'multiValues' : rear.multiValues
                    } for rear in trim.reartire_set.all()],
                }for trim in trims]
            
            return JsonResponse({'data' : data}, status=200)
        
        except AttributeError :
            return JsonResponse({'message' : 'AttributeError'}, status=400)
            
class TrimPathView(View) :
    def get(self, request, trim_id) :
        try : 
            trim          = Trim.objects.select_related('grade').prefetch_related('fronttire_set', 'reartire_set').get(id = trim_id)
            subModel      = SubModel.objects.select_related('yearType', 'submodelGroup').get(id = trim.grade.submodel.id)
            subModelGroup = SubModelGroup.objects.select_related('modelGroup').get(id = subModel.submodelGroup.id)
            modelGroup    = ModelGroup.objects.select_related('brand').get(id = subModelGroup.modelGroup.id)
            brand         = Brand.objects.get(id = modelGroup.brand.id)
            
            data = {
                'brandId'                   : brand.id,
                'brandName'                 : brand.brandName,
                'brandNameEng'              : brand.brandNameEng,
                'country'                   : brand.country,
                'isImported'                : brand.imImported,
                'brandImageUrl'             : brand.brandImageUrl,
                'brandUrl'                  : brand.brandUrl,
                'modelId'                   : modelGroup.id,
                'modelName'                 : modelGroup.modelName,
                'submodelGroupId'           : subModelGroup.id,
                'submodelGroupYearTypeFrom' : subModelGroup.submodelGroupYearTypeFrom,
                'submodelGroupYearTypeTo'   : subModelGroup.submodelGroupYearTypeTo,
                'submodelGroupName'         : subModelGroup.submodelGroupName,
                'submodelId'                : subModel.id,
                'submodelName'              : subModel.submodelName,
                'yearType'                  : subModel.yearType.yearType,
                'submodelImageUrl'          : subModel.submodelImageUrl,
                'gradeId'                   : trim.grade.id,
                'gradeName'                 : trim.grade.gradeName,
                'fuelType'                  : trim.grade.fuelType,
                'displacement'              : trim.grade.displacement,
                'trimId'                    : trim.id,
                'trimName'                  : trim.trimName,
                'salesCode'                 : trim.salesCode,
                'bodySize'                  : trim.bodySize,
                'bodyStyle'                 : trim.bodyStyle,
                'transmission'              : trim.transmission,
                'price'                     : trim.price,
                'priceUnit'                 : trim.priceUnit,
                'isRecommended'             : trim.isRecommended,
                'releaseDate'               : trim.releaseDate,
                'discontinuedDate'          : trim.discontinuedDate,
                'carTypeCode'               : trim.carTypeCode,
                'spec' : {
                    'front_tire' : [{
                        'name'        : front.name,
                        'value'       : front.value,
                        'unit'        : front.unit,
                        'multiValues' : front.multiValues
                    } for front in trim.fronttire_set.all()],
                    'rear_tire' : [{
                        'name'        : rear.name,
                        'value'       : rear.value,
                        'unit'        : rear.unit,
                        'multiValues' : rear.multiValues
                    } for rear in trim.reartire_set.all()],
                }
            }                
            
            return JsonResponse({'message' : data}, status=200)
        
        except Trim.DoesNotExist :
            return JsonResponse({'message' : 'Trim.DoesNotExist'}, status=400)