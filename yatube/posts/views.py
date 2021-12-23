from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_page
from django.urls import reverse
from django.db import IntegrityError

from .models import Post, Group, Follow
from .forms import PostForm, CommentForm
from yatube.settings import POSTS_PER_PAGE


User = get_user_model()


def _pagination(request, selector, count=POSTS_PER_PAGE):
    paginator = Paginator(selector, count)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


@cache_page(20)
def index(request):
    """Main page - dispalying the latest ten posts."""

    template = 'posts/index.html'
    posts = Post.objects.select_related('author', 'group').all()
    page_obj = _pagination(request, posts)
    context = {
        'page_obj': page_obj
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Filters by group and displays posts by ten per page."""

    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts_by_group = group.posts.all()
    context = {
        'group': group,
        'page_obj': _pagination(request, posts_by_group),
    }
    return render(request, template, context)


def profile(request, username):
    """Filters by author and displays posts by ten per page."""

    template = 'posts/profile.html'
    author = get_object_or_404(User, username=username)
    posts_by_author = author.posts.all()
    try:
        following = bool(author.following.filter(user=request.user))
    except Exception:
        following = False
    context = {
        'author': author,
        'page_obj': _pagination(request, posts_by_author),
        'following': following
    }
    return render(request, template, context)


def post_detail(request, post_id):
    """Filters by author and displays posts by ten per page."""

    template = 'posts/post_detail.html'
    post_by_text_id = get_object_or_404(Post, pk=post_id)
    form = CommentForm()
    comments = post_by_text_id.comments.all()
    context = {
        'post_by_text_id': post_by_text_id,
        'post_count': post_by_text_id.author.posts.count(),
        'comments': comments,
        'form': form
    }
    return render(request, template, context)


@login_required(redirect_field_name=None)
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None,)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=request.user)
    return render(request,
                  'posts/post_create.html',
                  {'form': form, 'is_edit': False})


@login_required(redirect_field_name=None)
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect('posts:post_detail', post_id)
    form = PostForm(request.POST or None,
                    files=request.FILES or None,
                    instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id)
    return render(request,
                  'posts/post_create.html',
                  {'form': form,
                   'is_edit': True,
                   'post_id': post_id}
                  )


@login_required(redirect_field_name=None)
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


@login_required(redirect_field_name=None)
def follow_index(request):
    template = 'posts/follow.html'
    authors_following = (Post.objects
                         .filter(author__following__user=request.user)
                         .select_related('author', 'group')
                         .all())
    page_obj = _pagination(request, authors_following)
    context = {
        'page_obj': page_obj
    }
    return render(request, template, context)


@login_required(redirect_field_name=None)
def profile_follow(request, username):
    author_obj = User.objects.get(username=username)
    try:
        Follow.objects.create(user=request.user, author=author_obj)
    except IntegrityError:
        pass
    return redirect(reverse('posts:profile', args=(username,)))


@login_required(redirect_field_name=None)
def profile_unfollow(request, username):
    try:
        author = User.objects.get(username=username)
        author.following.filter(user=request.user).delete()
    except Exception:
        print('No such user')
    return redirect('posts:profile', username=username)
