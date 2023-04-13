from .models import Article, Followers, Category, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse
from transliterate import slugify
from .services import get_article_list
from .forms import WriteArticleForm
User = get_user_model()


class GetForMainPage(View):
    """return html template with articles list"""

    def get(self, request):
        selected_category = request.GET.get('category')
        article_list = get_article_list(request, selected_category)
        return render(request, 'main_blog/main_page.html', {"article_list": article_list})


class GetArticle(View):
    """return html template with article data which taken by 'art_name'"""
    def get(self, request, art_name):
        article = get_object_or_404(Article, slug=art_name)
        comments = Comment.objects.filter(post=article.id)
        return render(request, 'main_blog/article.html', {"article": article, "comments": comments})


class GetUserPage(View):
    """return html template with user profile data which taken by 'username'"""
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
    def get(self, request):
        form = WriteArticleForm()
        return render(request, 'main_blog/create_article.html', {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            form = WriteArticleForm(request.POST, request.FILES)
            if form.is_valid():
                author = User.objects.get(id=request.user.id)
                title = form.cleaned_data.get('title')
                preview_pic = form.cleaned_data.get('uploaded_photo')
                content = form.cleaned_data.get('content')
                category_list = Category.objects.get(name=form.cleaned_data.get('category')).id
                slug = slugify(title)
                new_article = Article.objects.create(slug=slug, author=author, title=title,
                                                     preview_pic=preview_pic,
                                                     content=content)
                new_article.category_list.set([category_list])
                new_article.save()
                url = reverse('main_blog:blog')
                return HttpResponseRedirect(url)
            else:
                return render(request, 'main_blog/create_article.html', {"form": form})
        else:
            return HttpResponse("Вы не авторизированный пользователь!")