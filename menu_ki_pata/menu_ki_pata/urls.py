from django.contrib import admin
from django.urls import path, include  # Import include to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('menu.urls')),   # Include the app's URL configuration
]
