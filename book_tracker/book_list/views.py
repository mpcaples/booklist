from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_page_number = books.aggregate(Avg("page_count"))
    return render(request, "book_list/index.html", {
        "books": books, 
        "total_number_of_books": num_books,
        "average_page_count": avg_page_number
    })

def book_detail(request, slug): 
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_list/book_detail.html", {
        "title": book.title, 
        "author": book.author,
        "my_rating": book.my_rating, 
        "is_bestseller": book.is_bestseller,
        "page_count": book.page_count, 
        "year_published": book.year_published, 
        "publisher": book.publisher.name
    })


