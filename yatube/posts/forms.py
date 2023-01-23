from django.forms import ModelForm, Select, Textarea

from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        widgets = {
            'text': Textarea(attrs={'class': 'form-control'}),
            'group': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'text': 'Текст поста',
            'group': 'Группа',
        }
        help_text = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой бедет относиться пост',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
