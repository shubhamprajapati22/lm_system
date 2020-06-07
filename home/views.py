from django.shortcuts import render, HttpResponse
from books.models import IssueBooks, Books

# Create your views here.

def home(request):
    return render(request, 'index.html')


def profile(request):
    if request.user.is_authenticated == False:
        return HttpResponse(status = 400)

    issues = IssueBooks.objects.filter(user = request.user, is_return = False)


    return render(request, 'profile.html', {'issues':issues})



def about(request):
    return render(request, 'about.html')
