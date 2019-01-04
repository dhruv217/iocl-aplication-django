from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
