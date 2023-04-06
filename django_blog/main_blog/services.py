from .models import Article, Followers


def _get_base_data_template(category):
        if category:
            article_list = Article.objects.filter(category_list__name=category).order_by('-pub_date')[:10]
        else:
            article_list = Article.objects.all().order_by('-pub_date')[:10]
        return article_list


def get_article_list(request, selected_category):
    if request.user.is_authenticated:
        user = request.user
        subscribed_to = [users.id for users in Followers.objects.filter(subscribed_to=user.id)]
        if subscribed_to:
            if selected_category:
                article_list = Article.objects.filter(category_list__name=selected_category,
                                                      author__in=subscribed_to).order_by('-pub_date')[:10]
            else:
                article_list = Article.objects.filter(author__in=subscribed_to).order_by('-pub_date')[:10]
            if not article_list:
                article_list = _get_base_data_template(selected_category)
        else:
            article_list = _get_base_data_template(selected_category)

    else:
        article_list = _get_base_data_template(selected_category)

    return article_list
