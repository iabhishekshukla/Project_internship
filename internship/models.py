from django.db import models
from django.utils import timezone
#Create your models here.

class Provider(models.Model):
    providerid=models.CharField(max_length=45,primary_key=True)
    provpass=models.CharField(max_length=45)
    organizationname=models.CharField(max_length=100)
    ownername=models.CharField(max_length=100)
    email=models.EmailField(max_length=45)
    phonenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    domain=models.CharField(max_length=100)
    aboutorganisation=models.TextField()
    def _str_(self):
        return self.ownername
    
class ProgramDetails(models.Model):
    Providerid=models.ForeignKey(Provider,on_delete=models.DO_NOTHING)
    programname=models.CharField(max_length=100) 
    duration=models.CharField(max_length=20) 
    fees=models.CharField(max_length=100) 
    startdate=models.DateField(default=timezone.now)
    enddate=models.DateField(default=timezone.now)
    perquisite=models.CharField(max_length=255) 
    stipend=models.CharField(max_length=3) 
    description=models.CharField(max_length=255)  
    def _str_(self):
        return self.programname
    
class Feedback(models.Model):
    name=models.CharField(max_length=100) 
    email=models.CharField(max_length=20) 
    date=models.DateField(default=timezone.now)
    feedbacktext=models.TextField()
    rating=models.IntegerField()
    def _str_(self):
        return self.name
        
    
class Contactus(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    question=models.TextField()
    date=models.DateField(default=timezone.now)
    def _str_(self):
        return self.name

class Notice(models.Model):
    providerid=models.CharField(max_length=45)
    noticetopic=models.CharField(max_length=100)
    noticecontents=models.CharField(max_length=255)
    date=models.DateField(default=timezone.now)
    def _str_(self):
        return self.noticetopic


          
