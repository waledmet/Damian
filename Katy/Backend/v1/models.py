from django.db import models
import uuid 
from datetime import datetime



class BaseModel(models.Model):
    uuid = models.UUIDField( default = uuid.uuid4)
    create_at=models.DateTimeField(default=datetime.now)
    create_id=models.IntegerField()
    update_at=models.DateTimeField(blank=True,null=True)
    update_id=models.IntegerField(blank=True,null=True)
    is_open = models.BooleanField(default=True)
    
    class Meta:abstract = True


class customer(BaseModel):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    dob = models.DateTimeField(blank=True,null=True)
    

class quote(BaseModel):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=500)
    