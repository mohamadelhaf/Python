from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)


class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"
