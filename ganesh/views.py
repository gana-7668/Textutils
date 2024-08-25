
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def add(request):
    a=10
    b=20
    c=a+b
    return HttpResponse(c)

def analyze(request):
    # get the text
    removepunc=request.GET.get('removepunc','default')
    print(removepunc)
    djtext=request.GET.get('text','default')
    print(djtext)
# analyze the text
    return HttpResponse("removepunc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlinermove(request):
#     return HttpResponse("newline remove")

# def spaceremove(request):
#     return HttpResponse("space remove")

# def charcount(request):
    return HttpResponse("charcount")



