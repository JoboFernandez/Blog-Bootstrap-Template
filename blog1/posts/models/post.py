from django.db import models
from django.shortcuts import reverse
from tinymce import HTMLField

from . import Category, Author


class Post(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    overview = models.TextField()
    thumbnail = models.ImageField()
    featured = models.BooleanField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_modified = models.DateTimeField(auto_now_add=True)
    content = HTMLField('Content')
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})

    @property
    def comment_count(self):
        return self.comments.all().count()

    @property
    def view_count(self):
        return self.views.all().count()

    class Meta:
        ordering = ['-timestamp_created']
        get_latest_by = ['-timestamp_created']