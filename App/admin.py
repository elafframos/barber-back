from django.contrib import admin
from .models import Services

class adminServices(admin.ModelAdmin):
    list_display = ('agenda', 'value',)
    search_fields = ('model', )

admin.site.register(Services, adminServices, )