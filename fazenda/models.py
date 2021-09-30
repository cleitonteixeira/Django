from django.db import models

from django.contrib.auth.models import User

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Users(User):
    name = models.CharField(max_length=70, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self) -> str:
        return self.name

class Farms(Base):
    name = models.CharField(blank=False, unique=True, max_length=70)
    owner = models.CharField(blank=False, max_length=70)
    cpf = models.BigIntegerField(blank=False, unique=True)
    
    class Meta:
        verbose_name = "Farm"
        verbose_name_plural = "Farms"
    
    def __str__(self) -> str:
        return self.name

class Seasons(Base):
    farms = models.ForeignKey(Farms, related_name='seasons', on_delete=models.CASCADE)
    name = models.CharField(blank=False, unique=True, max_length=70)
    latitude = models.CharField(blank=False, unique=True, max_length=70)
    longitude = models.CharField(blank=False, unique=True, max_length=70)

    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Seasons"
    
    def __str__(self) -> str:
        return self.name