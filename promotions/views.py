from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Promotion

def promo_list(request):
    promos = Promotion.objects.all()
    return render(request, 'promotions/list.html', {'promos': promos})
