from django.contrib import admin
from django.urls import path, include
from . import views 
urlpatterns = [
    
    path('category/', views.AddCategory, name = 'add_category'),
    # path('books/', include('books.urls')),
    # path('categories/', include('categories.urls')),
    # path('reviews/', include('review.urls')),
    # path('transactions/', include('transactions.urls')),
 
]