from django.contrib.auth.models import User
from django.shortcuts import render
from .models import AddReview

def ReviewsView(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            reviews = request.POST['reviews']
            new_review = AddReview(login=user, review=reviews)
            new_review.save()
    return render(request, 'reviews/reviews.html', {})
