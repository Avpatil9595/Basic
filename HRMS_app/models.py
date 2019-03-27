from django.db import models
from datetime import *

# Create your models here.
class Skillset(models.Model):
    skill_name=models.CharField(max_length=100)

    class Meta:
        db_table='Skillset'


class Emp_info(models.Model):
    eid=models.IntegerField()
    fname=models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    pcontact=models.IntegerField()
    scontact=models.IntegerField(null=True)
    photo=models.ImageField(width_field=320,height_field=600)
    pemail=models.EmailField()
    semail=models.EmailField()
    skills=models.ForeignKey(Skillset,on_delete=models.CASCADE)

    created_at=models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    class Meta:
        db_table='Emp_info'