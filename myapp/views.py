from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView

from datetime import datetime as dt


from .forms import BlogForm,LoginForm
from .models import Blog


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


def blog(request):
    blogs = Blog.objects.all()
    params = {
        'blogs': blogs
    }
    return render(request, 'blog.html', params)

class indexview(ListView):
    template_name = 'index.html'
    model =Blog
    ordering = '-date'
    context_object_name = "blog_list"

class ContentCreate(CreateView):
   template_name = 'create.html'
   form_class = BlogForm
   success_url = reverse_lazy('myapp:index')
   def form_valid(self,form):
       Blog.date = dt.strptime(self.request.POST.get('date'), '%Y-%m-%d')
       return super().form_valid(form)

class tealist(ListView):
    template_name = 'tea.html'
    context_object_name = "tea_list"
    queryset = Blog.objects.filter(is_tea=True).order_by('-date')

class lacelist(ListView):
    template_name = 'works.html'
    queryset = Blog.objects.filter(is_tea=False).order_by('-date')
    context_object_name = "lace_list"


class blogdetail(DetailView):
    template_name = 'blog_detail.html'
    context_object_name = "blog_detail"
    model = Blog

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('myapp:create')

    def form_valid(self, form):
        passcord = '01234567'
        if passcord==form.data.get('pscord'):
            return super().form_valid(form)
        else:
            return redirect('myapp:index')

