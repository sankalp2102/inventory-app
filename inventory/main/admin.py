from django.contrib import admin
from .models import Club, InventoryItem, Request, Transaction
# Register your models here.

admin.site.register(Club)
admin.site.register(InventoryItem)
admin.site.register(Request)
admin.site.register(Transaction)