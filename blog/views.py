from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import MonthArchiveView

from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post

class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.published.all()
    date_field = 'created'
    context_object_name = 'posts'