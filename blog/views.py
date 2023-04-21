from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

def single_post_page(request,pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post':post
        }
    )



# FBV 방식 CBV로 쉽게 해보자!
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )