from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'hour', 'num_of_people', 'phone_number', 'note']

    def clean_num_of_people(self):
        num_of_people = self.cleaned_data['num_of_people']
        if num_of_people <= 0:
            raise forms.ValidationError("Il numero di persone deve essere maggiore di zero.")
        return num_of_people

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            phone_number = int(phone_number)
            if not (1000000000 <= phone_number <= 9999999999):
                raise forms.ValidationError("Il numero di telefono deve essere compreso tra 1000000000 e 9999999999.")
        except ValueError:
            raise forms.ValidationError("Il numero di telefono deve essere un valore numerico.")

        return phone_number

    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'hour': forms.TimeInput(attrs={'type': 'time'}),
    }
