from django.contrib import admin
from .models import Review # Проверьте, что в models.py модель называется Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text',)