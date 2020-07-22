from django.db import models

# Create your models here.

class List(models.Model):
	item = models.CharField(max_length=100,default='Blank item')
	desc = models.CharField(max_length=200,default='Blank desc')



