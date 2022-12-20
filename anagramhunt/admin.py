from django.contrib import admin
from .models import AddScore

@admin.register(AddScore)
class ScoreAdmin(admin.ModelAdmin):
    model = AddScore
    list_display = ['username', 'score','scoreM']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created')
        return ()



