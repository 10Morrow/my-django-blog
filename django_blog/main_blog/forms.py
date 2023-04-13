from django import forms
from .models import Article, Category


class WriteArticleForm(forms.ModelForm):
    preview_pic = forms.ImageField()
    title = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Выберите категорию")
    class Meta:
        model = Article
        fields = ('preview_pic', 'title', 'content', 'category')
