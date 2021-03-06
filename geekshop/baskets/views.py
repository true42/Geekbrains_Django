from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string

from baskets.models import Baskets
from mainapp.models import Product

@login_required
def basket_add(request, id):
    user_select = request.user
    product = Product.objects.get(id=id)
    baskets = Baskets.objects.filter(user=user_select, product=product)

    if baskets:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Baskets.objects.create(user=user_select, product=product, quantity=1)

    products = Product.objects.all()
    context = {'products': products}
    result = render_to_string('mainapp/includes/card.html', context)
    return JsonResponse({'result': result})

@login_required
def basket_remove(request, basket_id):
    Baskets.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Baskets.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Baskets.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/basket.html', context)
        return JsonResponse({'result': result})
