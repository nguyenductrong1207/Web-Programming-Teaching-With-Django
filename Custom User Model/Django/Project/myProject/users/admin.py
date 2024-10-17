from django.contrib import admin                                # HP 10 L3
from django.contrib.auth.admin import UserAdmin                 # HP 10 L3

from .forms import CustomUserCreationForm, CustomUserChangeForm # HP 10 L3
from .models import CustomUser                                  # HP 10 L3

class CustomUserAdmin(UserAdmin):                               # HP 10 L3
    add_form = CustomUserCreationForm                           # HP 10 L3
    form = CustomUserChangeForm                                 # HP 10 L3
    model = CustomUser                                          # HP 10 L3

admin.site.register(CustomUser, CustomUserAdmin)                # HP 10 L3
