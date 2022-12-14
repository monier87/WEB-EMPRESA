from django.contrib import admin
from .models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'update')
    list_display=('title','created', 'update')
    
admin.site.register(Service, ServiceAdmin)
    
