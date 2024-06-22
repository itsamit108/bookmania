from django.urls import path

from . import views

# URL configuration for the books app. Maps URL patterns to views.


urlpatterns = [
    path("", views.BookListView.as_view(), name="book.all"),
    path("<int:pk>", views.BookDetailView.as_view(), name="book.show"),
    path("<int:id>/review", views.review, name="book.review"),
    path("<str:author>", views.author, name="author.books"),
]
