from django.urls import path

from template_app.views import isitnewyea

urlpatterns = {
    path('isitnewyear/', isitnewyea)

}