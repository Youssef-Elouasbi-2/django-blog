

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from django.db.models import Q
from blog.forms import PostForm

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post = post.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('/posts')
        else:
            return HttpResponse('ERROR')
    else:
        form = PostForm()
        return render(request, 'post_add.html', {'form': form})
    
def view_posts(request):
    search = request.GET.get('search')
    if(search is not None):
        posts = Post.objects.filter(
            Q(title__contains=search) | Q(text__contains=search)
        ).order_by('-createddate')
    else: 
      posts = Post.objects.all()
    return render(request, 'view_posts.html', {'posts':posts, 'search': search})