from django.shortcuts import render, HttpResponse, redirect
from .models import Books, IssueBooks
from django.contrib import messages
from django.utils import timezone


# Create your views here.

def issuebooks(request):
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


    return render(request, 'issuebooks.html', {'books' : books})


def issue(request):
    if request.method == "POST":
        bookcode = request.POST['bookcode']
        book = Books.objects.get(code=bookcode)

        if book.no_of_copies == 0:
            return HttpResponse(status = 403)

        allissue = IssueBooks.objects.filter(user = request.user, is_return = False)
        no_of_books = allissue.count()

        request.session['re_issue'] = False

        if no_of_books < 3:
            request.session['max_issue'] = False


            if IssueBooks.objects.filter(code = book, user = request.user, is_return = False).exists():
                request.session['re_issue'] = True
                messages.error(request, "book is allready issued")
                print(" book is allready isssued")
                return redirect('/books/issuebooks/issue')
            book.no_of_copies-= 1
            info = IssueBooks.objects.create(code = book, user = request.user)
            book.save()
            info.save()

            return render(request, 'issue.html', {'infos' : info })
        else:
            request.session['max_issue'] = True
    return render(request, 'issue.html')




def returnbooks(request):
    issues = IssueBooks.objects.filter(user = request.user, is_return = False)
    if request.method == 'POST':
        book_return_code = request.POST['book_return']
        book_return = IssueBooks.objects.get(code = book_return_code, user = request.user, is_return = False)
        book_return.is_return = True
        book_return.returndate = timezone.now()
        book_return.save()
        book = Books.objects.get(code = book_return.code.code)
        book.no_of_copies += 1
        book.save()


    return render(request, 'returnbooks.html', {'issues' : issues})

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

    return unique_list

