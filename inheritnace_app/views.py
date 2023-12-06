from django.shortcuts import render


# Create your views here.
def first_view(request):
    return render(
        request,
        'inheritnace_app/first.html',
    )


def second_view(request):
    return render(
        request,
        'inheritnace_app/second.html',
    )