from django.urls import path
from .views import GuestListView, GuestDetailView, GuestCreateView, GuestUpdateView, GuestDeleteView, BookingListView, BookingDetailView, BookingCreateView

app_name = 'bookndine'

urlpatterns = [
    # Guests
    path('guests/', GuestListView.as_view(), name='guest-list'),
    path('guests/<int:pk>/', GuestDetailView.as_view(), name='guest-detail'),
    path('guests/add/', GuestCreateView.as_view(), name='guest-add'),
    path('guests/<int:pk>/edit/', GuestUpdateView.as_view(), name='guest-edit'),
    path('guests/<int:pk>/delete/', GuestDeleteView.as_view(), name='guest-delete'),

    # Bookings
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/add/', BookingCreateView.as_view(), name='booking-add'),
]
