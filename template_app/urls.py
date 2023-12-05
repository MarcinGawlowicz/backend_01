from django.urls import path

from template_app.views import isitnewyea, template_view

urlpatterns = {
    path('isitnewyear/', isitnewyea),
    path('', template_view),
}