from typing import List
from django.contrib.auth import models
from django.forms import fields
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post

# django mixins for delete
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", 'body', 'author']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
