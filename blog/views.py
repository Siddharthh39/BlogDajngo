from django.shortcuts import render
from .models import Post
from django.http import Http404
# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts':posts}
    )

def post_details(request, id):
    try:
        post = Post.published.get(id=id)
    
    except Post.DoesNotExist:
        raise Http404("Post not found")
    
    return render(
        request,
        'blog/post/detail.html',
        {'post':post}
    )

