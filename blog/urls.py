from django.urls import path
from .views import PostListView, PostDetailView, PostMonthArchiveView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:year>/<str:month>/', PostMonthArchiveView.as_view(), name='archive_month'),
]