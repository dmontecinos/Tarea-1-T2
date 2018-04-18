from django.db import models

# Create your models here.



class Team(models.Model):
    nombre = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField()
    codeTeam = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    birthday =models.DateField()
    age = models.IntegerField()
    rut = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    height = models.FloatField()
    weight = models.FloatField()
    photograpy = models.ImageField()
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Match(models.Model):
    namematch = models.CharField(max_length=200)
    def __str__(self):
        return self.name
