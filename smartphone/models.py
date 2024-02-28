from django.db import models

class smartphone(models.Model):
    id = models.IntegerField(primary_key=True)
    id_operateur = models.ForeignKey(operateur, on_delete=models.CASCADE))
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id_operateur} {self.nom} {self.id}"

    class Meta:
        db_table = 'phone'