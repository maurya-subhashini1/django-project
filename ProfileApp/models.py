# from django.db import models
from djongo import models


class Profile(models.Model):
    _id=models.ObjectIdField()
    name=models.CharField(max_length=100 ,null=False)
    age=models.CharField(max_length=2)
    email=models.EmailField(max_length=100,null=False,unique=True)
    phone=models.CharField(max_length=100 ,null=False)
    password=models.CharField(max_length=50)

