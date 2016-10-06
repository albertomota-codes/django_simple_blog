from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views import generic
from .models import Post
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout
import forms
import logging

def logout_view(request):
    logout(request)
    return redirect('blog:index_posts')

class UserFormView(View):
    form_class    = UserForm
    template_name = "blog/registration_form.html"

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.username = username
            user.save()

            user = authenticate(username =username, password = password )

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("blog:index_posts")

        return render(request, self.template_name,{'form':form})


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

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user is not None:
            obj.user = self.request.user
            obj.save()        
        return super(PostCreateView, self).form_valid(form)

class PostDeleteView(generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index_posts')