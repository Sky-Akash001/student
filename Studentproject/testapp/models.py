from django.db import models

# Create your models here.
class Studentregister(models.Model):
    name=models.CharField(max_length=20)
    marks=models.IntegerField()
    
