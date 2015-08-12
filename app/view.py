from django.views.generic import ListView, DetailView

from .models import Post, Tag


class PostsListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('tag')
        if query:
            return Post.objects.filter(tags=Tag.objects.filter(name=query))
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['alltags'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['alltags'] = Tag.objects.all()
        return context
