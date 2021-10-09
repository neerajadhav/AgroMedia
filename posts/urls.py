from django.urls import path
from .views import PostDeleteView, PostUpdateView

app_name = 'posts'

urlpatterns = [
    path('<pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('<pk>/update', PostUpdateView.as_view(), name='post-update'),
]
