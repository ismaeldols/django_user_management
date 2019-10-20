from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'iban', 'is_superuser']


UserAdmin.add_form = CustomUserCreationForm
UserAdmin.add_form = CustomUserChangeForm
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'username', 'password1', 'password2', 'iban', 'is_superuser')
    }),
)

admin.site.register(CustomUser, CustomUserAdmin)
