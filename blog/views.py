from .models import Post
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posty': posts})

def get_absolute_url(self):
    return reverse("blog:post_detail",kwargs={'pk':self.pk})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

