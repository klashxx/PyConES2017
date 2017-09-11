from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ('username',)

    fields = ('username',
              ('first_name', 'last_name'),
              'email',
              'groups',
              'user_permissions',
              ('is_staff', 'is_active', ),
              ('last_login', 'date_joined'),
              ('direccion1', 'direccion2'),
              'telefono',
              ('ciudad', 'provincia',)
              )
