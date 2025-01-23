from django.urls import path
# from . views import UserRegistrationView, UserLoginView, UserLogoutView
from . import views
urlpatterns = [
    # path('bookadd/', UserRegistrationView.as_view(), name = 'add_book'),
    # path('register/', UserRegistrationView.as_view(), name = 'register'),
    # path('login/', UserLoginView.as_view(), name = 'login'),
    # path('login/', UserLogoutView.as_view(), name = 'logout'),
    path('book/', views.BookView.as_view(), name = 'books'),
    path('book/<slug:cat_slug>/', views.BookView.as_view(), name = 'filter_category'),
     path('detail/<int:id>/', views.BookDetail, name = 'details'),
    
]