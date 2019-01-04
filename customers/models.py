from django.db import models
from ioclApp import settings
from ioclApp.get_request_obj import get_request_obj

# Create your models here.


class Customer(models.Model):
    """
    Class that contains the petrol punp customer to iocl.
    """
    createdOn = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    address = models.TextField()
    photo_url = models.URLField(max_length=500)
    land_details = models.TextField()
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField()
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        """
        Add user foregin key to added_by property of current customer object on save.
        """
        if not self.pk:
            # Only set added_by during the first save.
            self.added_by = get_request_obj().user
        super().save(*args, **kwargs)
