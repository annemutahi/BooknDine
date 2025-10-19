from django.urls import path
from .views import staff_login, staff_logout, DashboardView, BookingStatusUpdateView, BookingListView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'staff'

urlpatterns = [
    path('login/', staff_login, name='login'),
    path('logout/', staff_logout, name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('update/<int:booking_id>/', BookingStatusUpdateView.as_view(), name='update_status'),

    # API endpoints
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/staff/', views.StaffListCreateView.as_view(), name='staff-list-create'),
    path('api/staff/<int:pk>/', views.StaffDetailView.as_view(), name='staff-detail'),
    path('api/auth/login/', views.staff_api_login, name='staff-login'),
    path('api/auth/logout/', views.staff_api_logout, name='staff-logout'),
    path('api/bookings/', BookingListView.as_view(), name='booking_list_api'),
    path('api/bookings/<int:pk>/', views.BookingDetailAPIView.as_view(), name='booking_detail_api'),
    path('api/bookings/<int:booking_id>/update-status/', views.update_booking_status, name='booking_status_update_api'),
]