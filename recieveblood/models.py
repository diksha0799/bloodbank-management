from django.db import models

class Hospital(models.Model):
    hospitalname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    bloodsample = models.CharField(max_length=5)
    current_bloodsample = models.CharField(max_length=50)

    
    def __str__(self):
       return self.hospitalname
       return self.hospitalname+ ' | Credit: ' +str(self.currentbloodsample)

       
            

class Reciever(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    bloodsample = models.CharField(max_length=5)

    def __str__(self):
       return self.name
  