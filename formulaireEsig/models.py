from django.db import models

# Create your models here.

class Sie_Utilisateur(models.Model):
    UTI_LOGIN = models.CharField(max_length=50)
    UTI_MDP = models.CharField(max_length=50)
    UTI_NOM = models.CharField(max_length=50)
    UTI_PRENOM = models.CharField(max_length=50)
    UTI_CIVILITE = models.CharField(max_length=1)
    UTI_EMAIL = models.CharField(max_length=50)
    UTI_SUPPRIME = models.BooleanField()

    def __str__(self):   #méthoce qui returne un string con el nombre de l'utilisateur
        return self.UTI_NOM