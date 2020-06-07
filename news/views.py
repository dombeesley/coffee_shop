from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.

def get_posts(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "news.html", {'posts': posts})