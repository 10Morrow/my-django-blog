from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', AuthenticationView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]