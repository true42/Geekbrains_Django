from django.contrib import admin

# Register your models here.
from mainapp.models import Product_Category, Product

admin.site.register(Product_Category)
admin.site.register(Product)
