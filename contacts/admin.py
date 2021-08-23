from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserChangeForm
    form = CustomUserCreationForm
    model = CustomUser
    list_display = ['first_name', 'email', 'tel', 'text', 'subject', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tel', 'text', 'subject',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tel', 'text', 'subject',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)