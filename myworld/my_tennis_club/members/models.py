from django.db import models

class member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone=models.IntegerField(null=True)
    datetime=models.DateField(null=True)