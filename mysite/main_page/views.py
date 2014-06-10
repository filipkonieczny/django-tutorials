from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("What up.\nGo to /polls/ or /admin/")
    return render(request, 'main_page/index.html')


def wtf(request):
    # return HttpResponse("WTF?!")
    return render(request, 'main_page/wtf.html')


def yauza(request):
    # return HttpResponse("Yauza!")
    return render(request, 'main_page/yauza.html')