from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Guests, Bookings, Table
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from .serializers import BookingSerializer, GuestSerializer, TableSerializer
from rest_framework import generics, permissions

class GuestCreateView(CreateView):
    model = Guests
    fields = ['name', 'email', 'phone_number']
    template_name = 'Book/guest_form.html'
    def form_valid(self, form):
        # Save the guest
        guest = form.save()
        # Store guest ID in session so Django “remembers” who they are
        self.request.session['guest_id'] = guest.id
        # Redirect to booking form
        return redirect('booking-add')
    
class GuestDetailView(DetailView):
    model = Guests
    template_name = 'Book/guest_detail.html'
    context_object_name = 'guest'
    
class BookingCreateView(CreateView):
    model = Bookings
    fields = ['guest', 'table', 'start_time', 'end_time', 'num_people', 'status']  # No staff or status here!
    template_name = 'Book/booking_form.html'
    success_url = reverse_lazy('booking-list')
    def form_valid(self, form):
        guest_id = self.request.session.get('guest_id')
        if guest_id:
            form.instance.guest_id = guest_id
        booking = form.save()
        return redirect('booking-confirmation', booking_id=booking.id)
    
class BookingListView(ListView):
    model = Bookings
    template_name = 'Book/bookings_list.html'
    context_object_name = 'bookings'
    ordering = ['-start_time']
    paginate_by = 10

class BookingDetailView(DetailView):
    model = Bookings
    template_name = 'Book/booking_detail.html'
    context_object_name = 'booking' 

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})

class GuestListCreateView(generics.ListCreateAPIView):
    queryset = Guests.objects.all()
    serializer_class = GuestSerializer

class GuestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guests.objects.all()
    serializer_class = GuestSerializer

class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDetailView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer