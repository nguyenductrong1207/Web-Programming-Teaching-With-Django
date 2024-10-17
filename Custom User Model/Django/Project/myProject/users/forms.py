from django import forms                                                # HP 10 L3
from django.contrib.auth.forms import UserCreationForm, UserChangeForm  # HP 10 L3
from .models import CustomUser                                          # HP 10 L3

class CustomUserCreationForm(UserCreationForm):                         # HP 10 L3
    class Meta(UserCreationForm.Meta):                                  # HP 10 L3
        model = CustomUser                                              # HP 10 L3
        # fields = UserCreationForm.Meta.fields + ('sex_choice',)         # HP 10 L3
        # fields = UserCreationForm.Meta.fields + ('age',)                # HP 10 L3
        # fields = UserCreationForm.Meta.fields + ('sex',)                # HP 10 L3
        # fields = UserCreationForm.Meta.fields + ('address',)            # HP 10 L3
        fields = ('username', 'email', 'age', 'address', 'sex',)        # HP 10 L4

class CustomUserChangeForm(UserChangeForm):                             # HP 10 L3
    class Meta:                                                         # HP 10 L3
        model = CustomUser                                              # HP 10 L3
        # fields = UserChangeForm.Meta.fields                             # HP 10 L3
        fields = ('username', 'email', 'age', 'address', 'sex',)        # HP 10 L4