from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('waiter', 'Waiter'),
        ('chef', 'Chef'),
    ]
    role = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

#signal to create or update staff profile when user is created or updated
@receiver(post_save, sender=User)
def create_or_update_staff_profile(sender, instance, created, **kwargs):
    # Only create/update for staff users
    if instance.is_staff:
        StaffProfile.objects.get_or_create(user=instance)
    else:
        StaffProfile.objects.filter(user=instance).delete()