from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price') # Поля, которые будут видны в таблице
    search_fields = ('name',)       # Строка поиска по названию