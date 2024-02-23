from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from .forms import CommentForm, FindByTag
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request,'myapp/blog.html',{
        "posts":posts,
        "form":FindByTag()
    })

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request,'myapp/detail.html',{
        "post":post,
        "comments":comments,
        "form":form
    })

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,id=post_id,status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'myapp/comment.html',{
        'post': post,
        'form': form,
        'comment': comment})

def posts_by_tag(request):
    tag_slug = request.POST['t']
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        # tag = get_object_or_404(Tag,slug=tag_slug).id
        print(tag)
        print(tag_slug)
    
    return HttpResponseRedirect(reverse('myapp:finded_posts_by_tag',args=[tag]))



def finded_posts_by_tag(request, tag):
    posts = Post.published.filter(tags__slug__in=[tag])
    #posts = Post.published.filter(tags__in=[tag])
    return render(request,'myapp/findedposts.html',{
        "posts":posts,
    })