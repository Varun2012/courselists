from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    level=models.CharField(max_length=25)
    t_ype=models.CharField(max_length=25)
    
    instructor=models.CharField(max_length=25)
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.text

    def pub_date_pretty(self):
        return self.date

    def lev(self):
        return self.level

    def typ(self):
        return self.t_ype

    def Instructor(self):
        return self.instructor
    
    
    
    
