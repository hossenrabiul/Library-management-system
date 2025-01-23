
from django.urls import path, include

urlpatterns = [

    path('accounts/', include('accounts.urls')),
    # path('books/', include('books.urls')),
    # path('categories/', include('categories.urls')),
    # path('reviews/', include('review.urls')),
    # path('transactions/', include('transactions.urls')),
 
]