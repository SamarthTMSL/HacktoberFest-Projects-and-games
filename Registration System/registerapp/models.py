from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12,default="9755478801")
    gender=models.CharField(max_length=50,default="m")
    dob=models.CharField(max_length=20,default="2002-05-27")
    profession=models.CharField(max_length=50,default="Job")
    course=models.CharField(max_length=50,default="c++")
    def __str__(self):
        return str(self.id) + ':' + self.name + ':' + self.email+':'+str(self.phone)+':'+self.gender+":"+str(self.dob)+":"+self.profession+':'+self.course
    
