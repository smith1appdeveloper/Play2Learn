from django.contrib import admin
from .models import AddReview

@admin.register(AddReview)
class ReviewAdmin(admin.ModelAdmin):
    model = AddReview
    list_display =  ['login', 'review']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created')
        return ()


