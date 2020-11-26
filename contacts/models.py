from datetime import datetime

from django.db import models


class Contact(models.Model):
    """ A model that hold a contact info """

    listing = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    listing_id = models.IntegerField()
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
