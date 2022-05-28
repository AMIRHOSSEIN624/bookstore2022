from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomCreatUserForm, CustomChangeForm
from .models import CustomUser


class CustomAdmin(UserAdmin):
    add_form = CustomCreatUserForm
    form = CustomChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


admin.site.register(CustomUser, CustomAdmin)
