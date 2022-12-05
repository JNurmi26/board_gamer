from django.db import models

# Create your models here.
class Game(models.Model):
    """A game the user wants to interact with"""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text