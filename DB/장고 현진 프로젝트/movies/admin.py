from django.contrib import admin
from .models import Movie

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Movie, Admin)