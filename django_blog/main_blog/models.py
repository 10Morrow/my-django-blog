from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.name}"


# Create your models here.
class Article(models.Model):
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=255)
    preview_pic = models.ImageField(upload_to='photos/')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category_list = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Followers(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')

