from django.urls import path
from .views import *

app_name = 'main_blog'
urlpatterns = [
    path('', GetForMainPage.as_view(), name='blog'),
    path('article/<slug:art_name>/', GetArticle.as_view(), name='article'),
    path('<slug:username>/', GetUserPage.as_view(), name='username'),
]