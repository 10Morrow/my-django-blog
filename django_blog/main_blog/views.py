from .models import Article, Followers, Category, Comment
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class GetForMainPage(View):
    def get(self, request):
        article_list = [article.title for article in Article.objects.all()]
        return HttpResponse(f"Список статей: {article_list}")

    def post(self, request):
        selected_category = request.POST.get('category')
        return HttpResponse(f"Выбранная категория: {selected_category}")


class GetArticle(View):
    def get(self, request, art_name):
        article = get_object_or_404(Article, slug=art_name)
        comments = ''
        return HttpResponse(f"Статья: {article}")


class GetUserPage(View):
    def get(self, request, username):
        user = get_object_or_404(User, username__iexact=username)
        followers_count = len(Followers.objects.filter(subscribed_to = user.id))
        written_articles = Article.objects.filter(author=user.id)
        profile_data = {"username":user.username, "first_name":user.first_name, "second_name":user.last_name, "folowers_count":followers_count, "wrinnte_art":written_articles}
        return HttpResponse(f"информация о пользователе {user.username}: {profile_data}")
