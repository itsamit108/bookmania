from django.shortcuts import redirect, render
# Views for the books app. Imports Django generics for list and detail views of books. Imports book models and forms. Defines list and detail views for books, a view to filter books by author, and a view to handle submitting reviews. The book list and detail views handle fetching and rendering books and related data like reviews and authors. The author view filters books to those matching the author name. The review view handles submitting a review form and redirecting.
from django.views.generic import DetailView, ListView

from books.form import ReviewForm
from books.models import Book, Review


class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = context["book"].review_set.order_by("-created_at")
        context["authors"] = context["book"].authors.all()
        context["form"] = ReviewForm()
        return context


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {"book_list": books}
    return render(request, "books/book_list.html", context)


def review(request, id):
    if request.user.is_authenticated:
        newReview = Review(book_id=id, user=request.user)
        form = ReviewForm(request.POST, request.FILES, instance=newReview)
        if form.is_valid():
            form.save()
    return redirect(f"/book/{id}")
