from django.db import models

class Reservation(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com')
    date_rdv = models.DateField()
    heure_rdv = models.TimeField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.date_rdv} {self.heure_rdv}"
