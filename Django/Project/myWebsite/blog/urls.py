from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView # HP 10 L1

urlpatterns = [
    path("", views.list, name='blog'), 
    path("<int:id>/", views.post, name='post'),
    
    # HP 10 L1
    path("post_new", BlogCreateView.as_view(), name='post_new'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name='post'),
    path("", BlogListView.as_view(), name='home'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]
