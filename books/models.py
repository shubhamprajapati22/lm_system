from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Books(models.Model):
    code = models.IntegerField(primary_key = True)
    name = models.TextField()
    author = models.TextField(blank = True)
    publication = models.TextField(blank = True)
    subject = models.TextField(blank = True)
    no_of_copies = models.IntegerField()


class IssueBooks(models.Model):
    code = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issuedate = models.DateField(default = timezone.now)
    returndate = models.DateField(default = (timezone.now()+timezone.timedelta(days=30)))
    is_return = models.BooleanField(default = False)

    def remaining_days(self):
        r = (self.returndate - timezone.now().date()).days
        return r

#print(timezone.now().date()+timezone.timedelta(days=30))
