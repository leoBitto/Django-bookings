from django import forms
from django.core.exceptions import ValidationError
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'hour', 'num_of_people', 'note']
        
    def clean_num_of_people(self):
        num_of_people = self.cleaned_data['num_of_people']
        if num_of_people <= 0:
            raise ValidationError("Il numero di persone deve essere maggiore di zero.")
        return num_of_people

    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'hour': forms.TimeInput(attrs={'type': 'time'}),
    }
