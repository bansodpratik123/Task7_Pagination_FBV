from django.contrib import admin
from .models import Laptops

# Register your models here.
class LaptopsAdmin(admin.ModelAdmin):
    list_display = ['Model_Name','Provider','RAM','ROM','Processor','Weight','Price']
admin.site.register(Laptops,LaptopsAdmin)