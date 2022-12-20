from django.contrib import admin
from django.urls import path
from users.views import MyAccountPageView
from .views import MathFactsView, MFAView, MFDView, MFMView, MFSView, FinalView, GametrackView, LeaderboardView

app_name = 'mathfacts'
urlpatterns = [
    path('mathfacts/', MathFactsView.as_view(), name='mathfacts'),
    path('mfa/', MFAView.as_view(), name='mfa'),
    path('mfd/', MFDView.as_view(), name='mfd'),
    path('mfm/', MFMView.as_view(), name='mfm'),
    path('mfs/', MFSView.as_view(), name='mfs'),
    path('final/', FinalView, name='final'),
    path('gametrackmf/', GametrackView, name='gametrackmf'),
    path('leaderboardmf/', LeaderboardView, name='leaderboardmf'),
]