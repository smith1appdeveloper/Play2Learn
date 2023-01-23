from django.contrib import admin
from .models import AddScoreM

@admin.register(AddScoreM)
class ScoreAdminM(admin.ModelAdmin):
    model = AddScoreM
    list_display =  ['username', 'score','scoreM']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created')
        return ()