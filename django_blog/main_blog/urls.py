from django.urls import path
from .views import *
from django_blog import settings
from django.conf.urls.static import static

app_name = 'main_blog'
urlpatterns = [
    path('', GetForMainPage.as_view(), name='blog'),
    path('create_article/', CreateArticle.as_view(), name='create_article'),
    path('article/<slug:art_name>/', GetArticle.as_view(), name='article_name'),
    path('<slug:username>/', GetUserPage.as_view(), name='username'),
]


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)