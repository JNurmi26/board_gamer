from django.db import models
from django.contrib.auth.models import User

ACTIVE_CHOICES = [
    (False, 'Free'),
    (True, 'In use'),
]

# Create your models here.
class Game(models.Model):
    """A game the user wants to interact with"""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    is_borrowed = models.BooleanField(default=False, choices=ACTIVE_CHOICES)
    borrower = models.ForeignKey('Gamer', on_delete=models.PROTECT, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text

class Gamer(models.Model):
    """Page user"""
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username