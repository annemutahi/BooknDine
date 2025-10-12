from django.urls import path
from .views import GuestCreateView, BookingCreateView, BookingListView, BookingDetailView, GuestDetailView, booking_confirmation
from . import views

urlpatterns = [
    path('guest/add/', GuestCreateView.as_view(), name='guest-add'),
    path('guest/<int:pk>/', GuestDetailView.as_view(), name='guest-detail'),
    path('bookings/add/', BookingCreateView.as_view(), name='booking-add'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/confirmation/<int:booking_id>/', views.booking_confirmation, name='booking-confirmation'),
]
