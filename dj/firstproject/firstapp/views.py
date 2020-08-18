from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('hello world')


def login(request):
    return HttpResponse("로그인되었습니다")


def signout(request):
    return HttpResponse("잘가~")

def home(request) :
    

    return render(request, 'home.html')

def result(request):
    textbox = request.POST["textbox"]
    cnt_space=0
    cnt =0

    for i in textbox:
        cnt_space += 1
    for i in textbox:
        if i != " ":
            cnt += 1

    return render(request, 'result.html', {'cnt_space' : cnt_space ,'cnt' : cnt})