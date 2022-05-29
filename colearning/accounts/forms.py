from django.forms import ModelForm
from .models import Majlis, Post, Comment


class MajlisForm(ModelForm):
    class Meta:
        model = Majlis
        fields = ["title", "description"]

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]