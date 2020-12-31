from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .models import Forum, Thread, Post
from django.views import generic
from .forms import ForumCreationForm, ThreadCreationForm, PostCreationForm
from django.contrib import messages
from django.urls import reverse


@login_required
def forums(request):
    context = {
        'forums': Forum.objects.all(),
    }
    return render(request, 'forum/forums.html', context)


def threads(request, pk):
    forum_ = Forum.objects.raw('SELECT * FROM forum_forum WHERE id = %s', [pk])
    threads = Thread.objects.filter(forum_id=pk)
    context = {
        'threads': threads,
        'forum': forum_[0]
    }
    return render(request, 'forum/threads.html', context)


def create_forum(request):
    if request.method == 'POST':
        form = ForumCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Forum Created!')
            return redirect('forum:forums')
    else:
        form = ForumCreationForm()
    return render(request, 'forum/create_forum.html', {'form': form})


def create_thread(request, pk):
    if request.method == 'POST':
        form = ThreadCreationForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.forum_id = pk
            print(thread)
            thread.creator = request.user
            thread.save()
            messages.success(request, f'Thread Added to {thread.forum}')
            return redirect('forum:forums')
    else:
        form = ThreadCreationForm()
    return render(request, 'forum/create_thread.html', {'form': form})


def thread_detail_view(request, pk):
    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.thread_id = pk
            post.save()
    else:
        form = PostCreationForm()
    posts = Post.objects.filter(thread_id=pk)
    thread = Thread.objects.raw('SELECT * FROM forum_thread WHERE id = %s', [pk])
    context = {
        'form': form,
        'posts': posts,
        'thread': thread[0]
    }
    return render(request, 'forum/thread_view.html', context)


