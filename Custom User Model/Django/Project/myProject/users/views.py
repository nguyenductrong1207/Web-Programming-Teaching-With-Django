from django.urls import reverse_lazy  # HP 10 L4
from django.views.generic import CreateView # HP 10 L4

from .forms import CustomUserCreationForm # HP 10 L4

class SignUpView(CreateView): # HP 10 L4
    form_class = CustomUserCreationForm # HP 10 L4
    success_url = reverse_lazy('login') # HP 10 L4
    template_name = 'signup.html' # HP 10 L4