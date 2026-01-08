from django.urls import path
from . import views

urlpatterns = [
    path("checkin/", views.checkin_page, name="checkin_page"),
    path("checkins/", views.checkin_list, name="checkin_list"),
]
