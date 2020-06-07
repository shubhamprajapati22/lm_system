from django.urls import path
from . import views

urlpatterns = [
    path('issuebooks/', views.issuebooks, name = 'issuebooks'),
    path('issuebooks/issue/', views.issue, name = "issue"),
    path('returnbooks/', views.returnbooks, name = 'returnbooks')

]
