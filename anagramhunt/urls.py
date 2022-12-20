from django.contrib import admin
from django.urls import path
from .views import AnagramHuntView, AHGameplayView, AHView, GametrackView, LeaderboardView

app_name = 'anagramhunt'
urlpatterns = [
    path('anagramhunt/', AnagramHuntView.as_view(), name='anagramhunt'),
    path('ah_gameplay/', AHGameplayView.as_view(), name='ah_gameplay'),
    path('ah_final/', AHView, name='ah_final'),
    path('gametrackah/', GametrackView, name='gametrackah'),
    path('leaderboardah/', LeaderboardView, name='leaderboardah'),
]