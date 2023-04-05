from .models import Article, Followers, Category, Comment
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import get_user_model, authenticate

from .services import get_article_list

User = get_user_model()


class GetForMainPage(View):
    """return html template with articles list"""
    @staticmethod
    def get(self, request):
        selected_category = request.GET.get('category')
        article_list = get_article_list(request, selected_category)
        return HttpResponse(f"Список статей: {article_list}")


class GetArticle(View):
    """return html template with article data which taken by 'art_name'"""
    @staticmethod
    def get(self, request, art_name):
        article = get_object_or_404(Article, slug=art_name)
        comments = Comment.objects.filter(post=article.id)
        return render(request, 'main_blog/article.html', {"article": article, "comments": comments})


class GetUserPage(View):
    """return html template with user profile data which taken by 'username'"""
    @staticmethod
    def get(self, request, username):
        user = get_object_or_404(User, username__iexact=username)
        followers_count = len(Followers.objects.filter(subscribed_to = user.id))
        written_articles = Article.objects.filter(author=user.id)
        profile_data = {"username": user.username, "first_name": user.first_name,
                        "second_name": user.last_name, "followers_count": followers_count,
                        "written_articles": written_articles}
        return render(request, 'main_blog/profile.html', profile_data)


class CreateArticle(View):
    """return html template with form for creating articles"""
    pass