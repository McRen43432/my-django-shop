from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Убедись, что в твоем models.py поля называются именно name и price
        fields = ['name', 'price']

        # Добавляем красивые названия для полей (вместо Name и Price)
        labels = {
            'name': 'Название товара',
            'price': 'Стоимость (₸)',
        }

        # Добавляем стили (классы) прямо в поля, чтобы они выглядели современно
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите название (например, Ноутбук)',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Укажите цену',
            }),
        }