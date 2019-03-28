from django.db import models
from datetime import *
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

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


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)




class Education(models.Model):

      emp_id = models.IntegerField(primary_key=True)
      DEGREES = (
          ('B.E', 'Bachelore of Engineering'),
          ('B.A', 'Bachelore of Arts'),
          ('B.C.A', 'Bachelore of Computer Application'),
          ('B.CS', 'Bachelor of Computer Science'),
          ('M.E', 'Master of Engineering'),
          ('M.C.A', 'Master of Computer Application')
      )

      college_name = models.TextField(max_length=255)
      degree = models.CharField(choices=DEGREES, max_length=4, verbose_name='Degree Name')
      fromyear = models.IntegerField(('From Year'), default=1984, validators=[MinValueValidator(1984), max_value_current_year],choices=year_choices())
      toyear = models.IntegerField(('To Year'),default=1986 ,validators=[MinValueValidator(1984), max_value_current_year],choices=year_choices())



class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.TextField(null=False,max_length=255)