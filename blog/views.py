from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from  .forms import AddPostForm
# Create your views here.

def post_list(request):
    all_posts = Post.objects.all()
    return render(request,'blog/list.html',{'all_posts':all_posts})

def post_detail(request,slug):
    post_detail = Post.objects.get(post_slug=slug)
    return render(request,'blog/details.html',{'post':post_detail})

def add_Post (request):
    if request.method == 'POST':  ## اذ ادخل شخص معلومات في form
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/blog')
    else:
        form = AddPostForm()

    return render(request,'blog/add_post.html',{'form':form})

def post_edit(request,slug):
    posts = get_object_or_404(Post,post_slug=slug)

    if request.method == 'POST':  ## اذ ادخل شخص معلومات في form
        form = AddPostForm(request.POST, request.FILES ,instance = posts)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/blog')
    else:
        form = AddPostForm(instance = posts)

    return render(request,'blog/edit_post.html',{'form':form})

def delete_List(request,slug):
    post = Post.objects.get(post_slug=slug)
    
    if request.method == "POST":
        post.delete()
        return redirect('/blog')
    
    return render(request,'blog/delete_post.html',{'post':post})