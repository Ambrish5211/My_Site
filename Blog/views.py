from datetime import date
from .models import Post

from django.shortcuts import render



# Create your views here.

def get_date(post):
  return post['date']

def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": Post.objects.all()
    })



def post_detail(request, slug):
    identified_post = next(post for post in Post.objects.all() if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })