from django.urls import path # HP 10 L4
from .views import SignUpView # HP 10 L4

urlpatterns = [ # HP 10 L4
    path("signup/", SignUpView.as_view(), name="signup"), # HP 10 L4
]
