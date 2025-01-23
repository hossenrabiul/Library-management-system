from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-md',
                'placeholder': 'Write your comment here...',
                'rows': 4,  # Number of rows in the textarea
            }),
        } 