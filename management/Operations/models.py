from django.db import models
from accounts.models import *


class Category(models.Model):
    nom=models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
          return self.nom

class Projet(models.Model):
    titre=models.CharField(max_length=100)
    date_debut=models.DateField()
    date_fin=models.DateField(null=True)
    desc=models.TextField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    employe=models.ManyToManyField(Employe)
    def __str__(self):
            return self.titre

class Tache(models.Model):
    OPEN = 'Open'
    RUNNING = 'Running'
    PAUSED ='Paused'
    DONE = 'Done'
    STATUS_TACHE=(
        (OPEN,'Open'),
        (RUNNING,'Running'),
        (PAUSED,'Paused'),
        (DONE,'Done'),)
    nom=models.CharField(max_length=100)
    debut=models.DateField()
    fin=models.DateField()
    duration=models.IntegerField()
    desc=models.TextField()
    status = models.CharField(max_length=7,default=OPEN,choices=STATUS_TACHE,blank=False,null=True)
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class RessourceMateriel(models.Model):
    nom=models.CharField(max_length=100)
    desc=models.TextField(max_length=200)
    tache=models.ManyToManyField(Tache)

    def __str__(self):
        return self.nom