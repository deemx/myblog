from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import render_to_response

from .models import Post, Tag
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

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['alltags'] = Tag.objects.all()
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context
