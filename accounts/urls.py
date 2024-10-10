from django.urls import path, include
from .views import *


urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
]
