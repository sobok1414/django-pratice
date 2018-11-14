from django.shortcuts import render
from myBlog.models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    # 주요 객체 생성
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # 사용가능한 책
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
    }

    # 컨텍스트 변수와 함께 index.html을 랜더링한다.
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

    context_object_name = 'my_book_list'
    queryset = Book.objects.filter(title__icontains='war')[:5]
    template_name = 'books/my_arbitrary_template_name_list.html'

class BookDetailView(generic.DetailView):
    model = Book