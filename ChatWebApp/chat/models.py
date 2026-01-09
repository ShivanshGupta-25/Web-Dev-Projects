from django.db import models
from datetime import datetime

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    msg = models.TextField()
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000000)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

