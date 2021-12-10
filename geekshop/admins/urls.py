
from django.urls import path
from admins.views import index, UserCreateView, UserUpdateView, UserDeleteView, ProductListView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView, ProductCategoryListView, ProductCategoryCreateView, \
    ProductCategoryUpdateView, ProductCategoryDeleteView, UserListView

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view() , name='admin_users'),
    path('users_create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users_update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users_delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products_create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products_update/<int:pk>', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products_delete/<int:pk>', ProductDeleteView.as_view(), name='admin_products_delete'),
    path('categories/', ProductCategoryListView.as_view(), name='admin_categories'),
    path('categories_create/', ProductCategoryCreateView.as_view(), name='admin_categories_create'),
    path('categories_update/<int:pk>', ProductCategoryUpdateView.as_view(), name='admin_categories_update'),
    path('categories_delete/<int:pk>', ProductCategoryDeleteView.as_view(), name='admin_categories_delete'),
]

