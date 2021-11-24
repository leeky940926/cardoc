from django.db   import models

from core.models import TimeStampModel

class Brand(TimeStampModel) :
    brandName     = models.CharField(max_length=20)
    brandNameEng  = models.CharField(max_length=20)
    country       = models.CharField(max_length=20)
    imImported    = models.BooleanField(default=False)
    brandImageUrl = models.CharField(max_length=500)
    brandUrl      = models.CharField(max_length=500)
    
    class Meta :
        db_table = 'brands'

class ModelGroup(TimeStampModel) :
    brand     = models.ForeignKey(Brand, on_delete=models.CASCADE)
    modelName = models.CharField(max_length=20)
    
    class Meta :
        db_table = 'model_groups'

class SubModelGroup(TimeStampModel) :
    submodelGroupYearTypeFrom = models.PositiveIntegerField()
    submodelGroupYearTypeTo   = models.PositiveIntegerField()
    submodelGroupName         = models.CharField(max_length=20)
    modelGroup                = models.ForeignKey(ModelGroup, on_delete=models.CASCADE)
    
    class Meta :
        db_table = 'submodel_groups'

class AvailableYearType(TimeStampModel) :
    yearType        = models.PositiveIntegerField()
    
    class Meta :
        db_table = 'year_types'
        
class SubModel(TimeStampModel) :
    submodelName     = models.CharField(max_length=20)
    submodelNameEng  = models.CharField(max_length=20)
    yearType         = models.ForeignKey(AvailableYearType, on_delete=models.CASCADE)
    submodelImageUrl = models.CharField(max_length=500)
    submodelGroup    = models.ForeignKey(SubModelGroup, on_delete=models.CASCADE)
    
    class Meta :
        db_table = 'submodels'

class Grade(TimeStampModel) :
    gradeName    = models.CharField(max_length=20)
    fuelType     = models.CharField(max_length=20)
    displacement = models.PositiveIntegerField()
    submodel     = models.ForeignKey(SubModel, on_delete=models.CASCADE)
    
    class Meta :
        db_table = 'grades'

class Trim(TimeStampModel) :
    trimName         = models.CharField(max_length=20)
    salesCode        = models.PositiveIntegerField()
    bodySize         = models.CharField(max_length=5)
    bodyStyle        = models.CharField(max_length=20)
    transmission     = models.CharField(max_length=20)
    price            = models.PositiveIntegerField()
    priceUnit        = models.PositiveIntegerField()
    isRecommended    = models.BooleanField(default=False)
    releaseDate      = models.DateField(null=True)
    discontinuedDate = models.DateField(null=True)
    carTypeCode      = models.PositiveIntegerField()
    grade            = models.ForeignKey(Grade, on_delete=models.CASCADE)
    user             = models.ManyToManyField('users.User', through='TrimUser')
    
    class Meta :
        db_table = 'trims'
        
class TrimUser(TimeStampModel) :
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    trim = models.ForeignKey(Trim, on_delete=models.CASCADE)
    
    class Meta :
        db_table  = 'trims_users'
        
class FrontTire(TimeStampModel) :
    name        = models.CharField(max_length=20)
    value       = models.CharField(max_length=20)
    unit        = models.CharField(max_length=20)
    multiValues = models.CharField(max_length=20)
    trim        = models.ForeignKey(Trim, on_delete=models.CASCADE)
    
    class Meta :
        db_table = 'front_tires'

class RearTire(TimeStampModel) :
    name        = models.CharField(max_length=20)
    value       = models.CharField(max_length=20)
    unit        = models.CharField(max_length=20)
    multiValues = models.CharField(max_length=20)
    trim        = models.ForeignKey(Trim, on_delete=models.CASCADE)
    
    class Meta :
        db_table = 'rear_tires'