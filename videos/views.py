from django.views.generic import ListView, DetailView

from .models import Video

class VideoListView(ListView):
    model = Video
    context_object_name = 'videos'

class VideoDetailView(DetailView):
    model = Video