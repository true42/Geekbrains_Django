from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.views.generic import FormView, UpdateView

from authapp.models import User
from baskets.models import Baskets
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from mainapp.mixin import BaseClassContextMixin, UserDispatchMixin


class LoginListView(LoginView, BaseClassContextMixin):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    title = 'Geekshop - Авторизация'


class RegisterListView(FormView, BaseClassContextMixin):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    title = 'Geekshop | Регистрация'
    success_url = reverse_lazy('authapp:login')

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, 'Вы успешно зарегистрировались!')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, form.errors)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
        return render(request, self.template_name, {'form': form})

    def send_verify_link(self, user):
        verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учётной записи {user.username} пройдите по ссылке'
        messages = f'Для подтверждения учётной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, messages, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activate_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activate_key and not user.is_activation_key_expires():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(self, user)
            return render(self, 'authapp/verification.html')

        except Exception as e:
            return HttpResponseRedirect(reverse('index'))





class ProfileFormView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    title = 'Geekshop - Профиль'


    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, "Вы успешно изменили профиль")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)




class Logout(LogoutView):
    template_name = 'mainapp/index.html'
