from core.models import TimeStampModel
from django.db   import models

class User(TimeStampModel) :
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=500)
    
    class Meta :
        db_table = 'users'