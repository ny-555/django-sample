from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, welcome to Yuki's site. This site is made by Django.")