from django.db import models
from tkinter import CASCADE
from django.db import models

class Guest(models.Model):
    Email = models.EmailField(max_length=25)
    Name = models.CharField(max_length=25)
    Arival = models.DateField()
    Departure = models.DateField()
    RoomType = models.CharField(max_length=100,  null=True, blank=True)
    Price = models.IntegerField(null=True)
    Nights = models.IntegerField(null=True)
    Total = models.IntegerField(null=True)
    Message = models.TextField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.Email

class Room(models.Model):
    Type = models.CharField(max_length=100)
    Price = models.IntegerField()
    def __str__(self):
        return self.Type


        

