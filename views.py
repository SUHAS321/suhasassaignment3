from django.shortcuts import render
from django.http import HttpResponse


# View for the index page
def index(request):
    return render(request, 'index.html')

# View to show tasks for a given day
def monday(request):
    return render(request,'monday.html')

def tuesday(request):
    return render(request,'tuesday.html')

def wednesday(request):
    return render(request,'wednesday.html')

def thursday(request):
    return render(request,'thursday.html')

def friday(request):
    return render(request,'friday.html')

def saturday(request):
    return render(request,'saturday.html')

def sunday(request):
    return render(request,'sunday.html')


