from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("What up. Go to /polls/ or /admin/")