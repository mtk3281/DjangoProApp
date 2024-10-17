from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
import markdown
from django.utils.safestring import mark_safe
from django.contrib import messages
import logging

@login_required
def add_post_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'add_post.html', {'form': form})



def blog_post_detail_view(request, year, month, day, post):
    post = get_object_or_404(BlogPost, slug=post,
                             created_at__year=year,
                             created_at__month=month,
                             created_at__day=day)
    post.content = mark_safe(markdown.markdown(post.content))
    comments = post.comments.filter(active=True)
    new_comment = None
    messages.success(request, 'Comment added successfully')
            
    # Log the messages
    message_list = list(messages.get_messages(request))
    logging.debug(f"Messages: {message_list}")
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, 'blog_post_detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'form': form
    })