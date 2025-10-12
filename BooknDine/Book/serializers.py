from rest_framework import serializers
from .models import Guests, Table, Bookings

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = ['id', 'name', 'email', 'phone_number']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'table_number', 'capacity', 'location']


class BookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(read_only=True)
    table = TableSerializer(read_only=True)

    guest_id = serializers.PrimaryKeyRelatedField(
        queryset=Guests.objects.all(), source='guest', write_only=True
    )
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), source='table', write_only=True
    )

    class Meta:
        model = Bookings
        fields = [
            'id', 'guest', 'table', 'guest_id', 'table_id',
            'num_people', 'start_time', 'end_time', 'status', 'staff'
        ]
