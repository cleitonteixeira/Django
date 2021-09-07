from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Users(Base):
    name = models.CharField(max_length=70, null=False)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(blank=False, max_length=70)

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
    name = models.CharField(blank=False, unique=True, max_length=70)
    latitude = models.CharField(blank=False, unique=True, max_length=70)
    longitude = models.CharField(blank=False, unique=True, max_length=70)

    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Seasons"
    
    def __str__(self) -> str:
        return self.name