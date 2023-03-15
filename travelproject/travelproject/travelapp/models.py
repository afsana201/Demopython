from django.db import models

# Create your models here.
class Place(models.Model):

    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class People(models.Model):

    pimg=models.ImageField(upload_to='pics')
    pname=models.CharField(max_length=250)
    pdetails=models.TextField()

    def __str__(self):
        return self.pname



