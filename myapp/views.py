from django.shortcuts import render
from celeryproject.celery import add
from .tasks import sub

# Create your views here.
def index(request):
    print("Request: ")
    # add.delay(10,5)
    result1 = add.delay(10,5)
    print("result-1: ", result1)

    result2 = sub.delay(10,5)
    print("result-2: ", result2)

    return render(request, "home.html")

def about(request):
    print("Request: ")
    return render(request, "about.html")

def contact(request):
    print("Request: ")
    return render(request, "contact.html")
