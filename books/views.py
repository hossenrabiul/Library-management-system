from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import BooksDetails
from categories.models import Categories
from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.edit import FormView
from django.views.generic import DeleteView
from .models import BooksDetails
from review.models import Review
from review.forms import ReviewForm
from transactions.models import Transaction
from transactions.constants import PARCHASED
from django.contrib import messages
# Create your views here.

class BookView(TemplateView):
    template_name = 'all_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = BooksDetails.objects.all()

        cat_slug  = kwargs.get('cat_slug',None) 

        if cat_slug:
            category = Categories.objects.get(slug=cat_slug)
            books = BooksDetails.objects.filter(category=category)

        context['books'] = books
        context['categorys'] = Categories.objects.all()

        return context

def BookDetail(request, id):
    book = BooksDetails.objects.get(pk = id)
    reviews = Review.objects.filter(book = book)
    profile = request.user.profile
    Check = Transaction.objects.filter(profile = profile, book = book, transaction_type = PARCHASED)
 
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            
            if not Check:
                messages.error(request, 'You Have Not Purchased This Book Yet, So you can not leave review!')
                return redirect('details', id = id)
            
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            fun = True
            messages.success(request, 'Your review have been submitted successfully')

            return redirect('details', id = id)
    else:
        review_form = ReviewForm()
    return render(request, 'books_details.html', {'book' : book, 'comments' : reviews, 'comment_form' : review_form})
    