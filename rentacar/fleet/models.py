from django.db import models
from django.contrib.auth.models import User

class book(models.Model):
    name=models.ForeignKey(User ,on_delete=models.CASCADE,null=True,blank=True)
    pickup = models.CharField(max_length=50)
    returns= models.CharField(max_length=50)
    pudate=models.DateField()
    rdate=models.DateField()
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phno=models.IntegerField()


    def __str__(self):
        return self.fullname

