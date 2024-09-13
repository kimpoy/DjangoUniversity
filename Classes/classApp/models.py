from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60,blank=True)
    CourseNumber = models.IntegerField()
    Instructor = models.CharField(max_length=60,default="",blank=True)
    Duration = models.FloatField()

    #objects = models.Manager()
    
