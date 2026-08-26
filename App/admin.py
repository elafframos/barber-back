from django.contrib import admin
from .models import User, Services, Appointment

class adminServices(admin.ModelAdmin):
    list_display = ('name', 'value', 'duration')
    search_fields = ('name', )

admin.site.register(Services, adminServices)

admin.site.register(User)