from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>/", views.user_detail),
    path("me/", views.MeView.as_view()),
]
