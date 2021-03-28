from django.db import models


class Message(models.Model):
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)