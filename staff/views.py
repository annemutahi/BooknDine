from django.shortcuts import render, get_object_or_404, redirect
from Book.models import Bookings
from .mixins import StaffRequiredMixin
from django.views.generic import ListView, TemplateView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, permissions
from .serializers import StaffProfileSerializer
from .models import StaffProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from Book.serializers import BookingSerializer
from django.middleware import csrf

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
        return redirect('/staff/dashboard/')

# API Views for StaffProfile 
class StaffListCreateView(generics.ListCreateAPIView):
    queryset = StaffProfile.objects.select_related('user')
    serializer_class = StaffProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffProfile.objects.select_related('user')
    serializer_class = StaffProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class BookingListView(generics.ListAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser]

class BookingDetailAPIView(generics.RetrieveAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser]

# Authentication APIs
@csrf_exempt
@api_view(['POST'])
@authentication_classes([])  # disable SessionAuthentication
@permission_classes([])      # make open for now
def staff_api_login(request):
    data = request.data if request.data else request.POST
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=400)

    user = authenticate(username=username, password=password)
    if user is not None and user.is_staff:
        login(request, user)
        response = Response({'message': 'Login successful'})
        response.set_cookie(key='sessionid', value=request.session.session_key, httponly=True)
        return response
    
    return Response({'error': 'Invalid credentials or not a staff user'}, status=400)

@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def staff_api_logout(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})

@csrf_exempt
@api_view(['PATCH'])
@permission_classes([permissions.IsAdminUser])
def update_booking_status(request, booking_id):
    try:
        booking = Bookings.objects.get(pk=booking_id)
    except Bookings.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)

    new_status = request.data.get('status')
    if not new_status:
        return Response({'error': 'Status field is required'}, status=400)

    booking.status = new_status
    booking.save()
    return Response({'message': 'Booking status updated successfully', 'booking_id': booking.id, 'status': booking.status})