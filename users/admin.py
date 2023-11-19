from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone_number',)
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone_number',)
    exclude = ('password',)
