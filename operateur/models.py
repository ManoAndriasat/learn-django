from django.db import models

class operateur(models.Model):
    id_operateur = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id_operateur} {self.nom}"
