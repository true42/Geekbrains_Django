from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product, ProductCategory


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


def products(request, id_category=None, page=1):
    category = ProductCategory.objects.all()
    if id_category:
        all_products = Product.objects.filter(category_id=id_category)
    else:
        all_products = Product.objects.all()

    paginator = Paginator(all_products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'Geekshop - Каталог',
        'menu_items': category,
        'products': products_paginator
    }
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
