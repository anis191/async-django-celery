from django.shortcuts import render
from celeryproject.celery import add
from .tasks import sub
from celery.result import AsyncResult

# Create your views here.
"""
def index(request):
    print("Request: ")
    result1 = add.delay(10,5)
    print("result-1: ", result1)
    result2 = sub.delay(10,5)
    print("result-2: ", result2)
    return render(request, "home.html")
"""

def index(request):
    result = add.delay(10,5)
    return render(request, "home.html", {'result' : result})

def check_result(request, task_id):
    # Retrive the task result detail using task id
    result = AsyncResult(task_id)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
    return render(request, "result.html", {'result': result})

def about(request):
    print("Request: ")
    return render(request, "about.html")

def contact(request):
    print("Request: ")
    return render(request, "contact.html")
