from django.shortcuts import render

# Create your views here.
def count(request) :
    return render(request, 'count.html')

def result1(request) :
    return render(request, 'result1.html')

def result2(request) :
    return render(request, 'result2.html')

