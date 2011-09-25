from django.db import models
from datetime import datetime
from person.models import Agent, Client

class Case(models.Model):
    client = models.ForeignKey(Client, blank=False)

    title = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
