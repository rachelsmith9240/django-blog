from django.urls import path
from blogging.views import PostListView, PostDetailView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
]