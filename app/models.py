from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{0}'.format(self.name)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    datestamp = models.DateTimeField()
    posts = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return '/{0}/'.format(self.id)
