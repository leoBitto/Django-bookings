from django.urls import path
from . import views

urlpatterns = [
    path('booking/list/', views.booking_list, name='booking_list'),
    path('booking/detail/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('booking/create/', views.booking_create, name='booking_create'),
    path('booking/update/<int:pk>/', views.booking_update, name='booking_update'),
    path('booking/delete/<int:pk>/', views.booking_delete, name='booking_delete'),
    path('calendar/month/', views.calendar_month_view, name='calendar_month_view'),
    path('calendar/week/', views.calendar_week_view, name='calendar_week_view'),
]
