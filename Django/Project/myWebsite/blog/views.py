from django.shortcuts import render
from .models import Post
from django.http import Http404  # Import Http404

from django.views.generic import ListView, DetailView                       # HP 10 L1
from django.views.generic.edit import CreateView, UpdateView, DeleteView    # HP 10 L1
from django.urls import reverse_lazy                                        # HP 10 L1

# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)

def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Bài Viết Không Tồn Tại")    
    
    return render(request, 'blog/post.html', {'post': post})

# HP 10 L1
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__'
    # more example: fields = ['title', 'content']  # Define the fields that will appear in the form
    success_url = reverse_lazy('home')
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')