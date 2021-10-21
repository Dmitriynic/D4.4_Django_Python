from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator

from .models import Post as PostModel
from .filters import PostFilter
from .forms import PostForm

class Posts(ListView):
    model = PostModel
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-datetime']
    paginate_by = 10

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


class SearchPosts(ListView):
    model = PostModel
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-datetime']
    paginate_by = 10

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


class PostDetailView(DetailView):
    template_name = 'flatpages/post_detail.html'
    queryset = PostModel.objects.all()

class PostCreateView(CreateView):
    template_name = 'flatpages/post_create.html'
    from_class = PostForm

class PostUpdateView(UpdateView):
    template_name='flatpages/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return PostModel.objects.get(pk=id)

class PostDeleteView(DeleteView):
    template_name='flatpages/post_delete.html'
    queryset=PostModel.objects.all()
    success_url='/news/'