from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView, ListView
from django.urls import reverse_lazy, reverse
from .forms import LoginForm, UpassForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model


# Create your views here.
class Login(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('sensors_app:sensors')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)        
        return super(Login, self).form_valid(form)


class Logout(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )


class Upass(LoginRequiredMixin, FormView):
    template_name = 'users/uppass.html'
    form_class = UpassForm
    success_url = reverse_lazy('users_app:login')
    login_url = reverse_lazy('users_app:login')

    def form_valid(self, form):  
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1']         
        )

        if user:
            new_pass = form.cleaned_data['password2'] 
            usuario.set_password(new_pass)
            usuario.save()

        logout(self.request)
        return super(Upass, self).form_valid(form)


class UsersList(LoginRequiredMixin, ListView):
    template_name = 'users/listusers.html'
    model = get_user_model()
    context_object_name = 'users'
    login_url = reverse_lazy('users_app:login')

    
    
    
  

    