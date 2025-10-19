from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Guests, Bookings, Table
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from .serializers import BookingSerializer, GuestSerializer, TableSerializer
from rest_framework import generics, permissions
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError

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
    fields = ['table', 'start_time', 'end_time', 'num_people']
    template_name = 'Book/booking_form.html'

    def form_valid(self, form):
        guest_id = self.request.session.get('guest_id')
        if not guest_id:
            messages.error(self.request, "Guest session not found. Please add guest details first.")
            return redirect('guest-form')
        guest = get_object_or_404(Guests, id=guest_id)
        form.instance.guest = guest
        form.instance.status = Bookings.Status.PENDING

        overlapping = Bookings.objects.filter(
            table=form.cleaned_data['table'],
            start_time__lt=form.cleaned_data['end_time'],
            end_time__gt=form.cleaned_data['start_time']
        )
        if overlapping.exists():
            form.add_error(None, ValidationError("This table is already booked for the selected time."))
            return self.form_invalid(form)

        same_guest = Bookings.objects.filter(
            guest=guest,
            table=form.cleaned_data['table'],
            start_time__lt=form.cleaned_data['end_time'],
            end_time__gt=form.cleaned_data['start_time']
        )
        if same_guest.exists():
            form.add_error(None, ValidationError("You already have a booking for this table at this time."))
            return self.form_invalid(form)
        
        self.object = form.save()
        messages.success(self.request, f"Booking created successfully for table {self.object.table}.")
        return redirect(reverse('booking_confirmation', kwargs={'booking_id': self.object.id}))
    
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
    return render(request, 'Book/booking_confirmation.html', {'booking': booking})

@method_decorator(csrf_exempt, name='dispatch')
class GuestListCreateView(generics.ListCreateAPIView):
    queryset = Guests.objects.all()
    serializer_class = GuestSerializer

@method_decorator(csrf_exempt, name='dispatch')
class GuestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guests.objects.all()
    serializer_class = GuestSerializer

@method_decorator(csrf_exempt, name='dispatch')
class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

@method_decorator(csrf_exempt, name='dispatch')
class TableDetailView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

@method_decorator(csrf_exempt, name='dispatch')
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer

@method_decorator(csrf_exempt, name='dispatch')
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer