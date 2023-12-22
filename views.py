from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Booking
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from .utils import Calendar
from .forms import BookingForm
from django.contrib import messages


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
            messages.success(request, "Prenotazione creata con successo!")
            return redirect('bookings:calendar_month')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = BookingForm()

    return redirect('bookings:calendar_month')


def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Prenotazione aggiornata con successo!")
            return redirect('calendar_month')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = BookingForm(instance=booking)

    return redirect('bookings:calendar_month')

@require_POST
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    return redirect('bookings:calendar_month')


def calendar_day_view(request, year, month, day):
    selected_day = datetime(year, month, day)
    bookings = Booking.objects.filter(date=selected_day)

    if request.method == 'POST' and 'view_details' in request.POST:
        # Se il form nel modal è inviato
        form = BookingForm(request.POST, instance=bookings.first())
        if form.is_valid():
            form.save()

    context = {
        'selected_day': selected_day,
        'bookings': bookings,
        'view_details': True,
        'prev_day': selected_day - timedelta(days=1),
        'next_day': selected_day + timedelta(days=1),
    }

    return render(request, 'booking_day_calendar.html', context)


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

    # Creazione di una lista di dizionari per rappresentare le prenotazioni
    booking_list = []
    for booking in bookings:
        form = BookingForm(instance=booking)  # Crea il form per l'istanza corrente
        booking_dict = {
            'id': booking.pk,
            'name': booking.name,
            'date': booking.date,
            'hour': booking.hour,
            'num_of_people': booking.num_of_people,
            'phone_number': booking.phone_number,
            'note': booking.note,
            'form': form,  # Aggiungi il form all'istanza
        }
        booking_list.append(booking_dict)

    form = BookingForm()
    context = {
        'calendar': mark_safe(html_cal),
        'bookings': booking_list,
        'form': form,
    }

    return render(request, 'booking_month_calendar.html', context)