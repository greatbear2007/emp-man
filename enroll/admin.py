from django.contrib import admin

# Register your models here.

from .models import Employee

@admin.register(Employee)
class EmplyeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','age', 'bonus', 'salary','address')