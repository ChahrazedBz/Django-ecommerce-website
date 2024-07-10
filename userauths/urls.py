from django.urls import path

from userauths.views import login_view, register_view

app_name = "userauths"

urlpatterns = [
    path("sign-up/", register_view, name="sign-up"),
    path("sign-in/", login_view, name="sign-in"),
]
