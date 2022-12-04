from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)

class SecurePassword(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_password", null=True, blank=True)
    name = models.CharField(max_length=240, null=True, blank=True)
    password = models.TextField(null=False, blank=False)
