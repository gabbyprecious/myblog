from django.urls import path, include
from blog import views


urlpatterns = [
    path("register/", views.Create_User.as_view()),
    path("site/", views.ExampleView.as_view()),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]