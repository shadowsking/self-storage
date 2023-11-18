from django.contrib import admin
from service.models import Client, TypeStorage, Address, Storage, Order

admin.site.register(Client)
admin.site.register(TypeStorage)
admin.site.register(Address)
admin.site.register(Storage)
admin.site.register(Order)
