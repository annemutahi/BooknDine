from django.db import models

class Guests(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.role}"
    
class Bookings(models.Model):
    guest = models.ForeignKey(Guests, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.enums.TextChoices('Status', 'PENDING CONFIRMED CANCELLED')
    staff = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.guest.name} from {self.start_time} to {self.end_time}"
    
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    location = models.enums.TextChoices('Location', 'INDOOR OUTDOOR')

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"
    
class Bookings_Table(models.Model):
    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('booking', 'table')

    def __str__(self):
        return f"Booking {self.booking.id} - Table {self.table.table_number}"    