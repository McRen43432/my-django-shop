from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ВОТ ЭТОЙ СТРОКИ У ТЕБЯ НЕ ХВАТАЕТ:
    path('dashboard/', views.admin_dashboard, name='dashboard'),

    # Эта строка у тебя уже есть:
    path('dashboard/add/', views.add_product, name='add_product'),
]