from django.shortcuts import HttpResponse, render


def hello_view(request):
    return HttpResponse("hello world")


def hello_eva(request):
    return HttpResponse("Hello, Eva!")


def hello_adam(request):
    return HttpResponse("Hello, Adam!")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name.title()}!")


def hello_template(request, name):
    return HttpResponse(f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
                <h1>Hello, {name}!</h1>
            </body>
        </html>
    """)


def hello_template2(request, name):
    return render(request, 'name_templates.html', context={'name': name})