from django.contrib import admin
from app.models import Order

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)