from django.urls import path
from .views import GuestCreateView, BookingCreateView, BookingListView, BookingDetailView, GuestDetailView, booking_confirmation
from . import views

urlpatterns = [
    path('guest/add/', GuestCreateView.as_view(), name='guest-add'),
    path('guest/<int:pk>/', GuestDetailView.as_view(), name='guest-detail'),
    path('bookings/add/', BookingCreateView.as_view(), name='booking-add'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/confirmation/<int:booking_id>/', views.booking_confirmation, name='booking-confirmation'),
    
    # API endpoints
    path('api/guests/', views.GuestListCreateView.as_view(), name='guest-list-create'),
    path('api/guests/<int:pk>/', views.GuestDetailView.as_view(), name='guest-detail'),
    path('api/tables/', views.TableListView.as_view(), name='table-list'),
    path('api/tables/<int:pk>/', views.TableDetailView.as_view(), name='table-detail'),
    path('api/bookings/', views.BookingListCreateView.as_view(), name='booking-list-create'),
    path('api/bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
]
