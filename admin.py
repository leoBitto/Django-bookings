from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'hour', 'num_of_people', 'phone_number')
    search_fields = ['name', 'date']
    list_filter = ['date']
    date_hierarchy = 'date'

admin.site.register(Booking, BookingAdmin)
