from django.shortcuts import render, redirect  # Добавили redirect
# Импортируем модель текущего приложения
from .models import Product
# Импортируем модели из других приложений
from promotions.models import Promotion
from reviews.models import Review

# Импортируем форму (создадим её следующим шагом в файле forms.py)
from .forms import ProductForm


# Главная страница магазина
def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


# Ваша новая красивая админка (Dashboard)
def admin_dashboard(request):
    # Собираем все данные из базы данных
    products = Product.objects.all()
    promos = Promotion.objects.all()
    reviews = Review.objects.all()

    # Передаем всё это в один шаблон
    context = {
        'products': products,
        'promos': promos,
        'reviews': reviews,
    }
    return render(request, 'store/dashboard.html', context)


# ФУНКЦИЯ ДОБАВЛЕНИЯ ТОВАРА (Дополняем здесь)
def add_product(request):
    if request.method == "POST":
        # Если админ нажал кнопку "Сохранить" (пришел POST запрос)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новый товар в базу
            return redirect('dashboard')  # Возвращаемся в твою админку
    else:
        # Если админ просто открыл страницу (пришел GET запрос)
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})