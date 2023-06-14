from django.contrib import admin
from django.urls import path
from .views import AboutUsView, contact_form, HomePageView, LoginView, devView, Random_AceView, Random_Ace_GainView, Random_Ace_LoseView, Random_Ace_GainMView, Random_Ace_LoseMView

app_name =  'pages'
urlpatterns = [
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('contact-us/', contact_form, name='contact-us'),
    path('', HomePageView.as_view(), name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('dev/', devView.as_view(), name='dev'),
    path('random_ace/', Random_AceView.as_view(), name='random_ace'),
    path('random_ace_gain/', Random_Ace_GainView.as_view(), name='random_ace_gain'),
    path('random_ace_lose/', Random_Ace_LoseView.as_view(), name='random_ace_lose'),
    path('random_ace_gainM/', Random_Ace_GainMView.as_view(), name='random_ace_gainM'),
    path('random_ace_loseM/', Random_Ace_LoseMView.as_view(), name='random_ace_loseM'),
]