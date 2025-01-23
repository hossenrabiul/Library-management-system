from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import BooksDetails 
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction
from transactions.constants import PARCHASED,DEPOSIT
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        # context['historys'] = Transaction.objects.filter(profile=self.request.user.profile)
        # context['return'] = Transaction.objects.filter(profile=self.request.user.profile,transaction_type=RETURN).count()
        context['purchase'] = Transaction.objects.filter(profile=self.request.user.profile,transaction_type__in= [PARCHASED]).count()
        # context['pending'] = Transaction.objects.filter(profile=self.request.user.profile,transaction_type=PARCHASED).count()
        return context