from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from django.utils.safestring import mark_safe
import calendar
from datetime import datetime, timedelta
from .utils import Calendar
from .forms import BookingForm

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_detail.html', {'booking': booking})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})

def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking_form.html', {'form': form})

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')

    return render(request, 'booking_confirm_delete.html', {'booking': booking})

def calendar_month_view(request):
    today = datetime.now()
    cal = Calendar(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    return render(request, 'booking_month_calendar.html', {'calendar': mark_safe(html_cal), 'bookings': Booking.objects.all()})

def calendar_week_view(request):
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    cal = Calendar(today.year, today.month)
    html_cal = cal.formatweek(week_start, week_end)
    return render(request, 'booking_week_calendar.html', {'calendar': mark_safe(html_cal), 'bookings': Booking.objects.all()})

