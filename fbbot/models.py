from registration.models import customer
from django.db import models

class partner(models.Model):
    Name = models.CharField(max_length=100)
    App_id = models.CharField(max_length=100)
    Page_id = models.CharField(max_length=100)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.Name