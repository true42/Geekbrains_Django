from django.shortcuts import render
from .models import Product, Product_Category


# Create your views here.
def base(request):
    return render(request, 'mainapp/base.html')


def index(request):
    context = {
        'title': 'Geekshop',
        'title_description': 'GeekShop Store',
        'description': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    all_products = Product.objects.all()
    category = Product_Category.objects.all()
    context = {
        'title': 'Geekshop - Каталог',
        'menu_items': category,
        'products': all_products
    }
    return render(request, 'mainapp/products.html', context)
