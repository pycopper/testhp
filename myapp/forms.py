from django import forms
from .models import Blog,Login


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('date', 'title', 'img', 'contents', 'is_tea',)

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('pscord', )
