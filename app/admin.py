from django.contrib import admin

from .models import Post, Tag
from .settings import settings


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '{0}js/tinymce/tinymce.min.js'.format(settings.STATIC_URL),
            '{0}js/tinymce/tinymce-init.js'.format(settings.STATIC_URL),
        )


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
