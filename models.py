from django.db import models


class Booking(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    hour = models.TimeField(blank=True, null=True)
    num_of_people = models.IntegerField(blank=True, null=True)    
    phone_number = models.CharField(max_length=10, blank=True, null=True)  
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} alle {self.hour} il {self.date}"
