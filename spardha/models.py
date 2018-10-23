# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import os

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class student(models.Model):
    name = models.CharField(max_length=20)
    sid = models.AutoField(primary_key=True)
    pic= models.ImageField(upload_to=get_image_path,blank=True,null=True)
    sex = models.CharField(max_length=1)
    weight = models.IntegerField()
    yearOfStudy = models.IntegerField()
    contact = models.BigIntegerField()
    
class events(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    category = models.CharField(max_length=20,null=True,blank=True)
    eventFor = models.CharField(max_length=1)
    
    class Meta:
        unique_together = ('name','category','eventFor')

    # yearOfStudy = models.DateTimeField(
    #         default=timezone.now)
    
	# class eventReg(models.Model):
	# 	eventName=models.ForeignKey('events.name' ,on_delete=models.CASCADE)
	# 	eventCategory=models.ForeignKey('events.category',on_delete=models.CASCADE )
	# 	eventFor=models.ForeignKey('events.eventFor',on_delete=models.CASCADE)
	# 	sid=models.ForeignKey('student.sid',on_delete=models.CASCADE)
	# 	isCaptain=models.BooleanField()	

