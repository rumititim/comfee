from django.contrib import admin
from app.models import Order
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from app.models import Client

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'client'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline, )



class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)