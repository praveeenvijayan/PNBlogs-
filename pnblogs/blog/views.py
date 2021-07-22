from django.db import models
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import addPostForm, editPostForm

# Create your views here.
# def blog(request):
#     return render(request, 'blog/post.html')

class blog(ListView):
    model = Post
    template_name = 'blog/post.html'
    ordering = ['-posted_date']
    # ordering = ['-id']


class blog_details(DetailView):
    model = Post
    template_name = 'blog/single-post.html' 

class add_blog(CreateView):
    model = Post
    form_class = addPostForm
    template_name = 'blog/add-post.html'
    # fields = '__all__'

class update_blog(UpdateView):
    model = Post
    form_class = editPostForm
    template_name = 'blog/edit-post.html'
    # fields = ['title', 'body']

class delete_post(DeleteView):
    model = Post
    form_class = editPostForm
    template_name = 'blog/delete-post.html'
    success_url = reverse_lazy('blog')


