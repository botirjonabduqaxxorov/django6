from django.shortcuts import render, get_object_or_404
from .models import Category, Book

def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, 'library_app/home.html', {'categories': categories, 'books': books})

def category_books(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = category.books.all()
    return render(request, 'library_app/category_books.html', {'category': category, 'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library_app/book_detail.html', {'book': book})
