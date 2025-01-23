from django import forms
from .models import BooksDetails

class BookForm(forms.ModelForm):
    class Meta:
        model = BooksDetails
        fields = '__all__'