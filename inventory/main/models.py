from django.contrib.auth.models import AbstractUser
from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)

    # Resolve related_name conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Use a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Use a unique related_name
        blank=True
    )

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    details = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='inventory_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Request(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    processed_at = models.DateTimeField(auto_now_add=True)