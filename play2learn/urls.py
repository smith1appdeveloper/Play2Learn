from django.contrib import admin
from django.urls import path, include


urlpatterns = [
     # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    # User Management
    path('', include('users.urls')), #connects url from new app to main views.
    path('account/', include('allauth.urls')),

    # Local Apps
    path('', include('anagramhunt.urls')),
    path('', include('mathfacts.urls')),
    path('', include('pages.urls')),
]