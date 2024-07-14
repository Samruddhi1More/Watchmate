from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('watch/', include('watchlist_app.api.urls')),  # Include URLs from watchlist_app
    path('login/', views.obtain_auth_token),
]
