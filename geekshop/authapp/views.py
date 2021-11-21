from django.shortcuts import render


def login(request):
    context = {
        'title': 'Geekshop | Авторизация'
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    context = {
        'title': 'Geekshop | Регистрация'
    }
    return render(request, 'authapp/register.html', context)
