from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # Root path
    path("profile/", views.profile, name="profile"), # Additional path
    path('vie-deli/', views.vie_deli, name='vie_deli'), # Additional path
    path('tu-nho/', views.tu_nho, name='tu_nho'), # Additional path
    path('mona-hotel/', views.mona_hotel, name='mona_hotel'), # Additional path
]
