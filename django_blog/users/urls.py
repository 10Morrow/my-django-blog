from django.urls import path
from .views import *


urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('login/', AuthenticationView.as_view()),
    path('logout/', LogoutView.as_view()),
]