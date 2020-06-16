from django.shortcuts import render, HttpResponse
from books.models import IssueBooks, Books
from django.contrib.auth.models import AnonymousUser

def home(request):
    try:
        issues = IssueBooks.objects.filter(user = request.user, is_return = False)
    except TypeError:
        issues = None

    if request.method == 'GET':
        books = []
        try:
            searchv = request.GET['search_value']
            try:
                books = Books.objects.filter(code__icontains = int(searchv))
            except ValueError:
                books += Books.objects.filter(name__icontains = searchv)
                books += Books.objects.filter(author__icontains = searchv)
                books += Books.objects.filter(publication__icontains = searchv)
                books += Books.objects.filter(subject__icontains = searchv)

                books = unique(books)

        except KeyError:
            books = Books.objects.all().order_by('code')
    return render(request, 'index.html', {'issues':issues, 'books' : books})



def profile(request):
    if request.user.is_authenticated == False:
        return HttpResponse(status = 400)

    issues = IssueBooks.objects.filter(user = request.user).order_by('is_return', 'returndate')


    return render(request, 'profile.html', {'issues':issues})



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

    return unique_list
