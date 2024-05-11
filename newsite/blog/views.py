from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from .models import Blog

from django.urls import reverse_lazy
# Create your views here.


class BlogView(ListView):

    model = Blog
    template_name = 'blog/blogs_list.html'
    queryset = Blog.objects.select_related('user')
    context_object_name = "blogs"


class CreateBlogView(CreateView):

    model = Blog
    template_name = 'blog/add_blog.html'
    fields = 'name', 'blog_text', 'image'
    success_url = reverse_lazy('blog:blogs')


    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user from the request
        return super().form_valid(form)
