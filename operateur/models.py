from django.db import models

class Operateur(models.Model):
    id_operateur = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    prix = None
    localisation = None

    def __str__(self):
        return f"{self.id_operateur} {self.nom}"

    class Meta:
        db_table = 'operateur'