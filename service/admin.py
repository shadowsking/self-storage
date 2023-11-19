from django.contrib import admin
from .models import TypeStorage, Address, Order, Storage


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('user', 'date_at', 'date_to',)
    list_filter = ('storage__type_storage__name', 'storage__address__name',)
    raw_id_fields = ('user', 'storage',)


@admin.register(Storage)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'type_storage')
    list_filter = ('type_storage__name', 'address__name',)


admin.site.register(TypeStorage)
admin.site.register(Address)
