from django.contrib import admin
from .models import Promotion # Проверьте, что в models.py модель называется Promotion

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')