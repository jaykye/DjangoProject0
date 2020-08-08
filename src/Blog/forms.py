from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:  # 아마도 overwriting일 것.
        model = Article
        fields = [
            'title',
            'body',
        ]

