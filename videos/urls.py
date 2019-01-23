from django.urls import path
from .views import VideoListView, VideoDetailView

app_name = 'videos'
urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
    path('<slug>/', VideoDetailView.as_view(), name='video_detail'),
]