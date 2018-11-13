from django.shortcuts import render
from myBlog.models import Book, Author, BookInstance, Genre

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
        'num_authros' : num_authors,
    }

    # 컨텍스트 변수와 함께 index.html을 랜더링한다.
    return render(request, 'index.html', context=context)

