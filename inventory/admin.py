from django.contrib import admin
from .models import Desktop,Laptop,Mobile
# Register your models here.

@admin.register(Desktop,Laptop,Mobile)  
class ViewAdmin(admin.ModelAdmin):
    exclude = ('id', )