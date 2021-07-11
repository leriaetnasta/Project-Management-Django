from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

    

class Employe(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_employe = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_responsable = models.BooleanField(default=False)

    HOMME = 'Homme'
    FEMME = 'Femme'
    AUTRE = 'Autre'

    SEXE = (
    (HOMME,'Homme'),
    (FEMME,'Femme'),
    (AUTRE,'Autre'),
    )

    MR = 'Mr'
    MME = 'Mme'

    TITRE = (
    (MR,'Mr'),
    (MME,'Mme')
    )
    ROLE=(
        ("COMPTABLE","Comptable"),
        ("DIRECTEUR","Directeur"),
        ("SECRETAIRE","Secretaire"),
        ("RESPONSABLE D'ACHAT","Responsable d'achat"),
        ("COMMERCIAL","Commercial"),
        ("CHEF DE SERVISE","Chef de service"),
        ("RESPONSABLE RH","Responsable RH"),
        ("TECHNICIEN","Technicien"),
        ("INGENIEUR","Ingenieur"),
    ) 
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length = 254,null=True)
    titre = models.CharField(max_length=4,default=MR,choices=TITRE,blank=False,null=True)
    sexe = models.CharField(max_length=8,default=HOMME,choices=SEXE,blank=False)
    ce=models.CharField(max_length=100)
    date_naissance=models.DateField()
    role = models.CharField(max_length=100, default=0, choices=ROLE)
    adresse=models.TextField()
    ville=models.CharField(max_length=100)
    telephone=models.CharField(max_length=20,default='+212600000000', help_text= 'Entrer un numero de telephone E.G 2126XXXXXXXX')
    cin=models.CharField(max_length=50)
    image=models.ImageField()
    def __str__(self):
          return self.nom

class Responsable(Employe):
    pass

class Admin(Employe):
    pass
