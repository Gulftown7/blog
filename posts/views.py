from django.http.response import HttpResponse


# Create your views here.

def post_home(requests):
    return HttpResponse("<h1>Gulftown</h1>")

