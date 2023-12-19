from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'hour', 'num_of_people')
    search_fields = ['name']
    list_filter = ['date']
    date_hierarchy = 'date'

admin.site.register(Booking, BookingAdmin)
