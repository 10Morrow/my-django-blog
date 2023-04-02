from django.urls import path
from .views import *

urlpatterns = [
    path('', GetForMainPage.as_view()),
    path('article/<slug:art_name>/', GetArticle.as_view()),
    path('<slug:username>/', GetUserPage.as_view()),
]