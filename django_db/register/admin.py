from django.contrib import admin

# Register your models here.

from .models import Hotel, Register

admin.site.register(Hotel)
admin.site.register(Register)