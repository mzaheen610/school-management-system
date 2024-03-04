"""
Model to store messages and notifications in the communication system.
"""

from django.db import models
from core.models import User

class Message(models.Model):
    """Model for messages."""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



