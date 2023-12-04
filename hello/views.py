from django.shortcuts import HttpResponse


def hello_view(request):
    return HttpResponse("hello world")


def hello_eva(request):
    return HttpResponse("Hello, Eva!")


def hello_adam(request):
    return HttpResponse("Hello, Adam!")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name.title()}!")
