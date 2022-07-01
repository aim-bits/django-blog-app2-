from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import UpdateView


# Create your views here.
class PostListView(ListView):
    model = Post
    
    
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    

class PostDetailView(DetailView):
    model = Post
    
    
class PostUpdateView(DetailView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    
    
class PostDeleteView(DetailView):    
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")