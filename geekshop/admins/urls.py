
from django.urls import path
from admins.views import index, admin_users_create, admin_users_update, admin_users_delete, admin_users, admin_products, \
    admin_products_create, admin_products_update, admin_products_delete, admin_categories, admin_categories_create, \
    admin_categories_update, admin_categories_delete

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users_create/', admin_users_create, name='admin_users_create'),
    path('users_update/<int:pk>', admin_users_update, name='admin_users_update'),
    path('users_delete/<int:pk>', admin_users_delete, name='admin_users_delete'),
    path('products/', admin_products, name='admin_products'),
    path('products_create/', admin_products_create, name='admin_products_create'),
    path('products_update/<int:pk>', admin_products_update, name='admin_products_update'),
    path('products_delete/<int:pk>', admin_products_delete, name='admin_products_delete'),
    path('categories/', admin_categories, name='admin_categories'),
    path('categories_create/', admin_categories_create, name='admin_categories_create'),
    path('categories_update/<int:pk>', admin_categories_update, name='admin_categories_update'),
    path('categories_delete/<int:pk>', admin_categories_delete, name='admin_categories_delete'),
]

