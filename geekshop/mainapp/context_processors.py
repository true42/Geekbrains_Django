from baskets.models import Baskets

def basket(request):
    baskets_list = []
    if request.user.is_authenticated:
        baskets_list = Baskets.objects.filter(user=request.user)

    return {
        'baskets': baskets_list
    }