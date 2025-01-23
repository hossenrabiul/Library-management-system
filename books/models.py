from django.db import models
from categories.models import Categories
from django.contrib.auth.models import User
# Create your models here.
class BooksDetails(models.Model):
    AuthorName = models.CharField(max_length=100)
    BookName = models.CharField(max_length=100, default=None)
    category = models.ManyToManyField(Categories, blank=True,related_name='books')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='books/media/uploads', blank = True, null = True)
    borrowing_price = models.DecimalField(max_digits=12, decimal_places=4)


  