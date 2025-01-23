from django.db import models
from books.models import BooksDetails
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(BooksDetails, related_name='review', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"