from django.contrib import admin
from django.contrib.auth.models import User
from .models import Movie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget']
    list_editable = ['rating', 'year', 'budget']
    ordering = ['rating', '-name']
    list_per_page = 5
