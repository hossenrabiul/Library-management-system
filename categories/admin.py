from django.contrib import admin
from . models import Categories
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('CategoryName',)}
    list_display = ['CategoryName', 'slug']

admin.site.register(Categories, CategoryAdmin)