
from django.urls import path

from baskets.models import baskets

app_name = 'baskets'
urlpatterns = [
    path('bascets/', baskets, name='baskets'),
]

