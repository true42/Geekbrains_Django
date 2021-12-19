from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminCreateForm, ProductAdminProfileForm, \
    ProductCategoryAdminCreateForm
from authapp.models import User
from mainapp.models import Product, ProductCategory
from mainapp.mixin import BaseClassContextMixin, UserDispatchMixin


class IndexTemplateView(TemplateView, BaseClassContextMixin, UserDispatchMixin):
    template_name = 'admins/admin.html'


class UserListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Админка | Пользователи'



class UserCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Создание пользователей'



class UserUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')
    form_class = UserAdminProfileForm
    title = 'Админка | Редактирование пользователей'


class UserDeleteView(DeleteView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')
    form_class = UserAdminProfileForm
    title = 'Админка | Удаление пользователей'


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    title = 'Админка | Продукты'


class ProductCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Создание продукта'


class ProductUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')
    form_class = ProductAdminProfileForm
    title = 'Админка | Редактирование продукта'


class ProductDeleteView(DeleteView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')
    form_class = ProductAdminProfileForm
    title = 'Админка | Удаление продукта'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductCategoryListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    title = 'Админка | Категории'


class ProductCategoryCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = ProductCategoryAdminCreateForm
    success_url = reverse_lazy('admins:admin_categories')
    title = 'Админка | Создание категории'


class ProductCategoryUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins:admin_categories')
    form_class = ProductCategoryAdminCreateForm
    title = 'Админка | Редактирование категории'


class ProductCategoryDeleteView(DeleteView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins:admin_categories')
    form_class = ProductCategoryAdminCreateForm
    title = 'Админка | Удаление категории'


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
