from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms

# Create your views here.

def AddCategory(request):
    if request.method == 'POST':
        category_form = forms.CategoriesForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('AddCategory')
    else:
        category_form = forms.CategoriesForm()
    return render(request, 'add_category.html',{'form' : category_form})