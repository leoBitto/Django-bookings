from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    hour = models.TimeField(blank=True, null=True)
    num_of_people = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_cliente + ' alle ' + self.ora_prenotazione + ' il ' + self.data_prenotazione
    

        

