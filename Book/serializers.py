from rest_framework import serializers
from .models import Guests, Table, Bookings
from django.core.exceptions import ValidationError

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = ['id', 'name', 'email', 'phone_number']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'table_number', 'capacity', 'location']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'

    def validate(self, data):
        table = data.get('table')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        guest = data.get('guest')

        overlapping = Bookings.objects.filter(
            table=table,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping.exists():
            raise serializers.ValidationError("This table is already booked for the selected time.")

        same_guest = Bookings.objects.filter(
            guest=guest,
            table=table,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if same_guest.exists():
            raise serializers.ValidationError("You already have a booking for this table at this time.")

        return data
