from django.http import request
from .models import Post
from django.contrib.auth import login
from django.db import models
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.detail import DetailView
from posts.models import Post, Comment
from django.views.generic import CreateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from posts.forms import PostForm, CommentForm


class PostList(ListView):
    model = Post
    http_method_name = ['GET']
    template_name = 'posts/post_list.html'


    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        post_list = Post.objects.all()
        context['post_list'] = post_list
        return context

class PostDetail(DetailView):
    model = Post


class CreatePost(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = reverse_lazy('detail')
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DraftList(ListView, LoginRequiredMixin):
    model = Post
    template_name = 'posts/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(draft=True).order_by('-create_date')

class PostDelete(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('posts:all')


@login_required
def post_draft(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.draft()
    return redirect("posts:detail", pk=pk)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.create_date = timezone.now()
    post.publish()
    return redirect("posts:detail", pk=pk)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("posts:detail", pk=post_pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user 
            comment.save()
            return redirect('posts:detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'posts/comment_form.html',{'form':form})
