from django.shortcuts import render, redirect
from django.views.generic import FormView
from . forms import UserRegistraionForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistraionForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)  # form_valid funtion call hobe  automatically jodi sob tik thake
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
    
def user_logout(request):
    if request.user.is_authenticated:
        logout(request) 
    return redirect('home')
