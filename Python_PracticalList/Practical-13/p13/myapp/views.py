from django.shortcuts import render
from .models import Book
# Create your views here.
def home(request):
    book = Book.objects.all()
    return render(request, 'myapp/home.html', {'book': book})