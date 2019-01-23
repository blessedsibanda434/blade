from django.views.generic import TemplateView

from blog.models import Post
from videos.models import Video

class HomeView(TemplateView):
    latest_videos = Video.objects.all()[:2]
    latest_posts = Post.objects.all()[:2]
    extra_context = {
        'latest_posts': latest_posts,
        'latest_videos': latest_videos
    }
    template_name = 'home.html'