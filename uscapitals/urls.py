from django.urls import path
from .views import USCapitalView, KeepGoingView, successView

app_name = 'uscapitals'
urlpatterns = [
    path('uscapitals/', USCapitalView.as_view(), name='uscapitals'),
    path('keepgoing/', KeepGoingView.as_view(), name='keepgoing'),
    path('success/', successView.as_view(), name='success'),
]