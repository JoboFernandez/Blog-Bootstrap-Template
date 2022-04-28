from django.views.generic.edit import DeleteView
from django.shortcuts import reverse

from ..models import Post


class PostDeleteView(DeleteView):
    template_name = 'posts/post_confirm_delete.html'
    model = Post
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('posts:list')