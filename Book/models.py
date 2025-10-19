from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Guests(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Table(models.Model):
    class Location(models.TextChoices):
        INDOOR = 'INDOOR', 'Indoor'
        OUTDOOR = 'OUTDOOR', 'Outdoor'

    table_number = models.IntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=10, choices=Location.choices, default=Location.INDOOR)

    def __str__(self):
        return f"Table {self.table_number} ({self.location}, Capacity: {self.capacity})"
       
class Bookings(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    guest = models.ForeignKey(Guests, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    num_people = models.PositiveIntegerField(default=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def clean(self):
        # Check overlapping bookings for the same table
        overlapping = Bookings.objects.filter(
            table=self.table,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)

        if overlapping.exists():
            raise ValidationError("This table is already booked for the selected time.")

        # Optional: prevent the same guest from double-booking
        same_guest = Bookings.objects.filter(
            guest=self.guest,
            table=self.table,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)

        if same_guest.exists():
            raise ValidationError("You already have a booking for this table at this time.")

    def save(self, *args, **kwargs):
        self.clean()  # run validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.guest.name} ({self.status})"
    