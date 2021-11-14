from django.shortcuts import render


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

    context = {
        'title': 'Geekshop - Каталог',
        'menu_items': [
            'Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'
        ],
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'price': 6_090,
                'photo': 'Adidas-hoodie.png',
            },
            {
                'name': 'Синяя куртка The North Face',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'price': 23_725,
                'photo': 'Blue-jacket-The-North-Face.png',
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'price': 3_390,
                'photo': 'Brown-sports-oversized-top-ASOS-DESIGN.png',
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'description': 'Плотная ткань. Легкий материал.',
                'price': 2_340,
                'photo': 'Black-Nike-Heritage-backpack.png',
            },
            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'price': 13_590,
                'photo': 'Black-Dr-Martens-shoes.png',
            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'price': 2_890,
                'photo': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
            },
        ]
    }
    return render(request, 'mainapp/products.html', context)
