from django.shortcuts import render, HttpResponse, redirect
from .models import Books, IssueBooks
from django.contrib import messages

# Create your views here.

def issuebooks(request):
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


            if IssueBooks.objects.filter(code = book, user = request.user).exists():
                request.session['re_issue'] = True
                messages.info(request, "book is allready issued")
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
        book_return = IssueBooks.objects.get(code = book_return_code, user = request.user)
        book_return.is_return = True
        book_return.save()
        book = Books.objects.get(code = book_return.code.code)
        book.no_of_copies += 1
        book.save()


    return render(request, 'returnbooks.html', {'issues' : issues})

