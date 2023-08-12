from django.contrib import admin
from django.urls import path
from .views import AboutUsView, contact_form, HomePageView, LoginView, devView, betaView, Random_AceView, Random_Ace_GainView, Random_Ace_LoseView, Random_Ace_GainMView, Random_Ace_LoseMView, Who_am_IView, Who_am_I_rulesView, Who_am_I2View, Final_TallyView, Who_am_I_endView, Final_Tally_UpView, Final_Tally_DownView, game_overView, game_over_View, twentyView

app_name =  'pages'
urlpatterns = [
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('contact-us/', contact_form, name='contact-us'),
    path('', HomePageView.as_view(), name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('dev/', devView.as_view(), name='dev'),
    path('beta/', betaView.as_view(), name='beta'),
    path('random_ace/', Random_AceView.as_view(), name='random_ace'),
    path('random_ace_gain/', Random_Ace_GainView.as_view(), name='random_ace_gain'),
    path('random_ace_lose/', Random_Ace_LoseView.as_view(), name='random_ace_lose'),
    path('random_ace_gainM/', Random_Ace_GainMView.as_view(), name='random_ace_gainM'),
    path('random_ace_loseM/', Random_Ace_LoseMView.as_view(), name='random_ace_loseM'),
    path('who_am_I/', Who_am_IView.as_view(), name='who_am_I'),
    path('who_am_I_rules/', Who_am_I_rulesView.as_view(), name='who_am_I_rules'),
    path('who_am_I2/', Who_am_I2View.as_view(), name='who_am_I2'),
    path('final_tally/', Final_TallyView.as_view(), name='final_tally'),
    path('Who_am_I_end/', Who_am_I_endView.as_view(), name='Who_am_I_end'),
    path('final_tally_up/', Final_Tally_UpView.as_view(), name='final_tally_up'),
    path('final_tally_down/', Final_Tally_DownView.as_view(), name='final_tally_down'),
    path('game_over/', game_overView.as_view(), name='game_over'),
    path('game_over_/', game_over_View.as_view(), name='game_over_'),
    path('twenty/', twentyView.as_view(), name='twenty'),
]