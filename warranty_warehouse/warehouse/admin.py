from django.contrib import admin
from .models import Order, StorageLocation, Part, LogEntry

admin.site.register(Order)
admin.site.register(StorageLocation)
admin.site.register(Part)
admin.site.register(LogEntry)
