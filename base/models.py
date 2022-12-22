from django.db import models
from django.contrib.auth.models import User

class SecurePassword(models.Model):
    # user = models.ForeignKey(User, related_name="user_password", on_delete=models.CASCADE, null=False, blank=True) # still thinking if it's on the right place
    name = models.CharField(max_length=240, null=True, blank=True)
    password = models.TextField(null=False, blank=False)

class Group(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    password = models.ManyToManyField(SecurePassword, on_delete=models.CASCADE, related_name="group_password", null=True, blank=True)
