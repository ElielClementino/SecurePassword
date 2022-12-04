from django.urls import path
from . import views


urlpatterns = [
    path("api/create_password", views.create_password)
]
