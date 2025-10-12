from django.urls import path
from .views import staff_login, staff_logout, DashboardView, BookingStatusUpdateView

app_name = 'staff'

urlpatterns = [
    path('login/', staff_login, name='login'),
    path('logout/', staff_logout, name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('update/<int:booking_id>/', BookingStatusUpdateView.as_view(), name='update_status'),
]