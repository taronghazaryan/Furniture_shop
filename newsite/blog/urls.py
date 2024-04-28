from django.urls import path
from .views import BlogView, CreateBlogView

app_name = 'blog'

urlpatterns = [
    path('all/', BlogView.as_view(), name='blogs'),
    path('add/', CreateBlogView.as_view(), name='add_blog'),
]
