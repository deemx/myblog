from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Post, Tag
from .settings import settings


class PostAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
