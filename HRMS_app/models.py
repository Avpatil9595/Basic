from django.db import models
from datetime import *

# Create your models here.
class Skillset(models.Model):
    skill_name=models.CharField(max_length=100)

    class Meta:
        db_table='Skillset'


