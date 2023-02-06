from django.shortcuts import render, redirect
from .models import Post
from django.views import generic
from .forms import PostForm
from slug import slug


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts_detail.html'


def novoPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.meu_slug = slug(post.titulo)
            post.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'novo_post.html', {'form': form})

