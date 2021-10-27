#instances of path
from django.urls import path
from .views import BlogListView, BlogDetailView

# path, view class that handles rendering,
# keyword argument to define the name
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]