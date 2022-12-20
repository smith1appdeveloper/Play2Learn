from django.contrib import admin
from django.urls import path
from .views import ReviewsView

app_name = 'reviews'
urlpatterns = [
    path('reviews/', ReviewsView, name='reviews'),
]