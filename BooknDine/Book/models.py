from django.db import models
from django.contrib.auth.models import User

class Guests(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    
class Bookings(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    guest = models.ForeignKey(Guests, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.guest.name} ({self.status})"
    
class Table(models.Model):
    class Location(models.TextChoices):
        INDOOR = 'INDOOR', 'Indoor'
        OUTDOOR = 'OUTDOOR', 'Outdoor'

    table_number = models.IntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=10, choices=Location.choices, default=Location.INDOOR)

    def __str__(self):
        return f"Table {self.table_number} ({self.location}, Capacity: {self.capacity})"
    
class Bookings_Table(models.Model):
    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('booking', 'table')

    def __str__(self):
        return f"Booking {self.booking.id} - Table {self.table.table_number}"    