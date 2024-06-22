# Register the Book and Author models with the admin site
# so they are displayed and editable in the admin interface.
from django.contrib import admin

from books.models import Author, Book

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
