from django.urls import path

from footer import views


app_name = "footer"

urlpatterns = [
    path("about.html", views.About.as_view(), name="about"),
]