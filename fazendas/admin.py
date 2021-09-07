from django.contrib import admin

from .models import Users, Farms, Seasons

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'created', 'modified')

@admin.register(Farms)
class FarmsAdmin(admin.ModelAdmin):
    list_display = ('id','name','owner','cpf','created', 'modified')

@admin.register(Seasons)
class Seasons(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude','created', 'modified')