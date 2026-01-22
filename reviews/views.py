from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Review

def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/list.html', {'reviews': reviews})
