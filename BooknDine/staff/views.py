from django.shortcuts import render, get_object_or_404, redirect
from Book.models import Bookings
from .mixins import StaffRequiredMixin
from django.views.generic import ListView, TemplateView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def staff_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('staff:dashboard')
        else:
            messages.error(request, 'Invalid credentials or not authorised.')
    return render(request, 'staff/login.html')

def staff_logout(request):
    logout(request)
    return redirect('staff:login')

class DashboardView(StaffRequiredMixin, TemplateView):
    template_name = 'staff/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Bookings.objects.all().order_by('-created_at')
        return context

class BookingStatusUpdateView(StaffRequiredMixin, View):
    template_name = 'staff/update_status.html'

    def get(self, request, booking_id):
        booking = get_object_or_404(Bookings, id=booking_id)
        return render(request, self.template_name, {'booking': booking})

    def post(self, request, booking_id):
        booking = get_object_or_404(Bookings, id=booking_id)
        new_status = request.POST.get('status')
        booking.status = new_status
        booking.save()
        messages.success(request, 'Booking status updated successfully!')
        return redirect('staff:dashboard')