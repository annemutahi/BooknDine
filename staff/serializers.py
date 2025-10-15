from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StaffProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class StaffProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StaffProfile
        fields = ['id', 'user', 'role']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        user.is_staff = True
        user.save()
        staff_profile = StaffProfile.objects.create(user=user, **validated_data)
        return staff_profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()

        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
