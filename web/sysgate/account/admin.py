from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', )
    list_filter = ('username',)
    contact_fields = (
        'direccion1',
        'direccion2',
        'ciudad',
        'provincia',
        'telefono',
    )
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Datos Contacto', {'fields': contact_fields}),
    )
