from django.urls import path
from . import views
#    path('bookings/', include('bookings.urls', namespace='bookings')),
app_name = 'bookings'
urlpatterns = [
    path('detail/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('create/', views.booking_create, name='booking_create'),
    path('update/<int:pk>/', views.booking_update, name='booking_update'),
    path('delete/<int:pk>/', views.booking_delete, name='booking_delete'),
    path('calendar/month/', views.calendar_month_view, name='calendar_month'),
    path('calendar/week/', views.calendar_week_view, name='calendar_week'),
    path('day/<int:year>/<int:month>/<int:day>/', views.calendar_day_view, name='calendar_day'),
]
