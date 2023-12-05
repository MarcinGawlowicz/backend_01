from datetime import datetime

from django.shortcuts import render


def isitnewyea(request):
    now = datetime.now()
    if now.month == 1 and now.day == 1:
        is_new_year = True
    else:
        is_new_year = False

    return render(
        request,
        'is_it_new_year.html',
        {
            'is_new_year': is_new_year
        }
    )


def template_view(request):
    fruits = [
        'jabłko',
        'banan',
        'mandarynki'
    ]

    return render(
        request,
        'template.html',
        {
            'fruits': fruits
        }
    )