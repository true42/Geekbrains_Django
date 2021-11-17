from django.shortcuts import render
import json


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
    with open('mainapp/fixtures/goods.json', 'r', encoding='UTF-8') as json_data:
        products_data = json.load(json_data)
    context = {
        'title': 'Geekshop - Каталог',
        'menu_items': [
            'Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'
        ],
        'products': products_data['products']
    }
    return render(request, 'mainapp/products.html', context)
