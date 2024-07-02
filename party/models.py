import uuid

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class CustomUser(AbstractUser):
    pass


class Party(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation = models.TextField()
    venue = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="organized_name")


    class Meta:
        verbose_name_plural = "parties"

    def __str__(self):
        return f"{self.venue} on {self.party_date}"
    


class Gift(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    gift = models.CharField(max_length=255)
    price = models.FloatField(blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.gift
    

class Guest(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    attending = models.BooleanField(default=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="guests")
    

    def __str__(self):
        return str(self.name)
    


