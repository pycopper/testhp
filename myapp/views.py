from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from myapp.models import Post, Category, Tag,Blog


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def blog(request):
    blogmodel ={'blogs': Blog.objects.all(),}
    return render(request, 'blog.html',blogmodel)

class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj

class IndexView(ListView):
    model = Post
    template_name = 'myapp/index.html'

class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))

class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))



