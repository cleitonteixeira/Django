import uuid
from django.db import models
from uuid import uuid4

# Create your models here.
class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=25, null=False)
    email = models.CharField(max_length=75, null=False)
    password = models.CharField(max_length=20)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)