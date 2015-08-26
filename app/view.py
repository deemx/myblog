from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .models import Post, Tag, Comments
from .forms import CommentModelForm


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


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentModelForm
    success_url = './'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['alltags'] = Tag.objects.all()
        context['comments'] = Comments.objects.filter(
            post_id=self.get_object().id)
        context['form'] = self.get_form(self.form_class)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return super(PostDetailView, self).get(
                request, *args, **kwargs)

    def form_valid(self, form):
        form_save = form.save(commit=False)
        form_save.post_id = self.get_object().id
        form_save.save()
        return super(PostDetailView, self).form_valid(form)
