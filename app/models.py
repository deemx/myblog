from django.db import models

from captcha.fields import CaptchaField
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{0}'.format(self.name)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    datestamp = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return '/{0}/'.format(self.id)


class Comments(models.Model):
    nickname = models.CharField(max_length=35)
    comment = models.TextField(default='')
    captcha = CaptchaField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
