from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello, this is hw7")
def home(request):
    return HttpResponse("Welcome to the homepage!")
