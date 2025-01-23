from django.db import models

# Create your models here.
class Categories(models.Model):
    CategoryName = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.CategoryName} : '