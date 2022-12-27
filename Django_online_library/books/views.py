from inspect import Parameter
from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

def books_view(request):
    template = 'books/books_list.html'
    Book_objects = Book.objects.all().order_by('pub_date').distinct()
    context = {'books':Book_objects}
    return render(request, template, context)

def paginator_books(request, param):
    template = 'books/books_list.html'
    CONTENT = Book.objects.all().order_by('pub_date')
    paginator = Paginator(CONTENT, 1)
    pages= [book['pub_date'].strftime("%Y-%m-%d") for book in Book.objects.order_by('pub_date').values('pub_date').distinct()]
    index_page = pages.index(param)
    page = paginator.get_page(index_page+1)
    previous_page = pages[index_page-1]   
    try:
        next_page = pages[index_page+1]
    except:
        next_page = pages[index_page]  
      
    context = {
        'books':  page.object_list,                    
        'page': page,
        'next_page':next_page,
        'previous_page':previous_page       
    }
    return render(request, template, context)
