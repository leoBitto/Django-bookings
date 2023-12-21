from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Booking
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from .utils import Calendar
from .forms import BookingForm


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST' and 'view_details' in request.POST:
        # Se il form nel modal è inviato
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
    
    return render(request, 'booking_month_calendar.html', {'booking': booking, 'view_details': True})


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_month_view')
    else:
        form = BookingForm()

    return redirect('calendar_month_view')

def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('calendar_month_view')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking_month_calendar.html', {'form': form})

@require_POST
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    return redirect('calendar_month_view')

def calendar_week_view(request):
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    cal = Calendar(today.year, today.month)
    calendar_html = mark_safe(cal.formatweek(week_start, week_end))

    return render(request, 'booking_week_calendar.html', {'calendar': calendar_html, 'bookings': Booking.objects.all()})


def calendar_month_view(request):
    today = datetime.now()
    year = today.year
    month = today.month

    cal = Calendar(year, month)
    html_cal = cal.formatmonth(withyear=True)

    # Filtra le prenotazioni solo per il mese corrente
    bookings = Booking.objects.filter(date__year=year, date__month=month)
    form = BookingForm()
    context = {
        'calendar': mark_safe(html_cal),
        'bookings': bookings,
        'form': form,
    }

    return render(request, 'booking_month_calendar.html', context)