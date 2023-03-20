from django.contrib import admin
from django.urls import path
from .views import AnagramHuntView, AHGameplayView, AHView, AHView2, AHViewVictory, GametrackView,  LeaderboardView

app_name = 'anagramhunt'
urlpatterns = [
    path('anagramhunt/', AnagramHuntView.as_view(), name='anagramhunt'),
    path('ah_gameplay/', AHGameplayView.as_view(), name='ah_gameplay'),
    path('ah_final/', AHView, name='ah_final'),
    path('ah_final2/', AHView2, name='ah_final2'),
    path('ah_victory/', AHViewVictory, name='ah_victory'),
    path('gametrackah/', GametrackView, name='gametrackah'),
    path('leaderboardah/', LeaderboardView, name='leaderboardah'),
]