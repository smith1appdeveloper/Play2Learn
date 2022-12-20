from django.contrib import admin
from django.urls import path
from .views import AboutUsView, contact_form, HomePageView

app_name = 'pages'
urlpatterns = [
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('contact-us/', contact_form, name='contact-us'),
    path('', HomePageView.as_view(), name='homepage'),

]