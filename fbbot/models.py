from django.db import models

from django.contrib.auth.models import User


class FBUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    psid = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.CharField(max_length=255, null=True, blank=True)
    locale = models.CharField(max_length=10, null=True, blank=True)
    timezone = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=64, null=True, blank=True)
    is_payment_enabled = models.BooleanField(default=False)


class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    page_id = models.CharField(max_length=100)
    app_id = models.CharField(max_length=255)
    token = models.CharField(max_length=500)

    def __str__(self):
        return self.name