from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm, RegisterForm

def home(request):
    posts=Post.objects.filter(status='PUBLISHED').order_by('-created_at')
    q=request.GET.get('q')
    if q: posts=posts.filter(title__icontains=q)
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'cms/home.html',{'posts':posts})

def register(request):
    form=RegisterForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('dashboard')
    return render(request,'registration/register.html',{'form':form})

@login_required
def dashboard(request):
    posts=Post.objects.filter(author=request.user)
    return render(request,'cms/dashboard.html',{'posts':posts})

@login_required
def create_post(request):
    form=PostForm(request.POST or None, request.FILES or None)
    if request.method=='POST' and form.is_valid():
        post=form.save(commit=False)
        post.author=request.user
        post.save()
        return redirect('dashboard')
    return render(request,'cms/post_form.html',{'form':form})

@login_required
def update_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.user!=post.author: return redirect('dashboard')
    form=PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method=='POST' and form.is_valid():
        form.save(); return redirect('dashboard')
    return render(request,'cms/post_form.html',{'form':form})

@login_required
def delete_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.user==post.author: post.delete()
    return redirect('dashboard')

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk,status='PUBLISHED')
    return render(request,'cms/post_detail.html',{'post':post})

@login_required
def profile(request):
    return render(request,'cms/profile.html')
