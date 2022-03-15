from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from myapp.models import Post, Category, Tag


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def recruit(request):
    return render(request, 'recruit.html')

def sitemap(request):
    return render(request, 'sitemap.html')

def menu(request):
    return render(request, 'menu.html')

def staff(request):
    return render(request, 'staff.html')

def works(request):
    return render(request, 'works.html')

def shop(request):
    return render(request, 'shop.html')

def access(request):
    return render(request, 'access.html')

def link(request):
    return render(request, 'link.html')

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



