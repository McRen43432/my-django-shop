from django.urls import path
from .views import promo_list

urlpatterns = [
    path('', promo_list),
]
