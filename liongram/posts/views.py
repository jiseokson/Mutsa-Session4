from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import ListView
from posts.forms import PostBaseForm, PostCreateForm

from posts.models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html', context)

def post_list_view(request):
    post_list = Post.objects.all()
    # Post.objects.filter(writer=request.user) # 현재 로그인한 사용자의 게시글 조회
    context = {
        'post_list': post_list,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/post_detail.html', {'post': post})

# @login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    elif request.method == 'POST':
        image = request.FILES.get('image')
        content = request.POST.get('content')
        Post.objects.create(
            image=image,
            content=content,
            # writer=request.user,
        )
        return redirect('index')
    
def post_create_form_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'posts/post_form2.html', context)
    else:
        form = PostBaseForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer = request.user,
            )
        return redirect('index')

def post_update_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'post': post,
        }
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        image = request.FILES.get('image')
        content = request.POST.get('content')
        if image:
            post.image.delete()
            post.image = image
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)

def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        return render(request, 'posts/post_confirm_delete.html', {'post': post})
    elif request.method == 'POST':
        post.delete()
        return redirect('index')


def url_view(request):
    return HttpResponse('<h1>url view</h1>')
    # return JsonResponse({'name': 'Jiseok'})

def url_parameter_view(request, username):
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'