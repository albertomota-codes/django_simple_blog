from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import generic
from .models import Post
from django.urls import reverse, reverse_lazy
import forms
import logging

logger = logging.getLogger(__name__)

class IndexPostView(generic.ListView):
    template_name = 'blog/index_posts.html'
    context_object_name = 'post_list'
    

    def get_queryset(self):
        a=self.request.GET.get('q', '')
        #return Post.objects.all()
        return Post.objects.filter(text__icontains=a) |  Post.objects.filter(title__icontains=a)

class ReadPostView(generic.DetailView):
    model = Post
    template_name = 'blog/readPost.html'


class UpdatePostView(generic.edit.UpdateView):
    model = Post
    #fields = ['title','text']
    template_name_suffix = '_update_form'
    form_class = forms.PostForm

    def get_success_url(self):
        return reverse('blog:index_posts')

class PostCreateView(generic.edit.CreateView):
    model = Post
    #fields = ['title','text','publication_date']
    form_class = forms.PostForm
    def get_success_url(self):
        return reverse('blog:index_posts')

class PostDeleteView(generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index_posts')