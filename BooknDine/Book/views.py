from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Guests, Bookings
from .mixins import StaffRequiredMixin

# --- Guests Views ---
class GuestListView(StaffRequiredMixin, ListView):
    model = Guests
    template_name = 'guests_list.html'


class GuestDetailView(StaffRequiredMixin, DetailView):
    model = Guests
    template_name = 'guest_detail.html'


class GuestCreateView(CreateView):
    model = Guests
    fields = ['name', 'email', 'phone_number']
    template_name = 'Book/guest_form.html'
    success_url = reverse_lazy('guest-list')


class GuestUpdateView(StaffRequiredMixin, UpdateView):
    model = Guests
    fields = ['name', 'email', 'phone_number']
    template_name = 'guest_form.html'
    success_url = reverse_lazy('guest-list')


class GuestDeleteView(StaffRequiredMixin, DeleteView):
    model = Guests
    template_name = 'guest_confirm_delete.html'
    success_url = reverse_lazy('guest-list')


# --- Bookings Views ---
class BookingListView(StaffRequiredMixin, ListView):
    model = Bookings
    template_name = 'bookings_list.html'


class BookingDetailView(StaffRequiredMixin, DetailView):
    model = Bookings
    template_name = 'booking_detail.html'


class BookingCreateView(CreateView):
    model = Bookings
    fields = ['guest', 'start_time', 'end_time', 'status', 'staff']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking-list')
