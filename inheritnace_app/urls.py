from django.urls import path

from inheritnace_app.views import first_view, second_view

app_name = "inheritnace_app"

urlpatterns = [
    path('first/', first_view, name='first_name'),
    path('second/', second_view, name='second_name')
]