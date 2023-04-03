from .models import Article, Followers, Category, Comment
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class GetForMainPage(View):

    @staticmethod
    def get_base_data_template(category):
        if category:
            article_list = Article.objects.filter(category_list__name=catalog).order_by('-pub_date')[:10]
        else:
            article_list = Article.objects.all().order_by('-pub_date')[:10]
        return article_list

    def get(self, request):
        selected_category = request.GET.get('category')
        if request.user.is_authentificate:
            user = request.user
            subscribed_to = [users.id for users in Followers.objects.filter(subscribed_to = user.id)]
            if subscribed_to:
                if selected_category:
                    article_list = Article.objects.filter(category_list__name=selected_category,
                                                          author__in=subscribed_to).order_by('-pub_date')[:10]
                else:
                    article_list = Article.objects.filter(author__in=subscribed_to).order_by('-pub_date')[:10]
                if not article_list:
                    article_list = self.get_base_data_template(selected_category)
            else:
                article_list = self.get_base_data_template(selected_category)

            return HttpResponse(f"Список статей: {article_list}")

        else:
            article_list = self.get_base_data_template(selected_category)
            return HttpResponse(f"Список статей: {article_list}")



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
