from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:pk>/", views.display_menu_items, name="menu_item"),
    
    # Add the API token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # This will enable the token authentication route
    
    # Optionally, you can add more views or endpoints as needed
]
