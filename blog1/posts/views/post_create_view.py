from django.views.generic.edit import CreateView
from django.shortcuts import redirect, reverse

from ..models import Post, Author


class PostCreateView(CreateView):
    template_name = 'posts/post_form.html'
    model = Post
    fields = ['title', 'thumbnail', 'categories', 'featured', 'overview', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.filter(featured=True)[:3]
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        previous_obj = Post.objects.latest('timestamp_created')
        obj = form.save(commit=False)
        obj.author = Author.objects.get(user=self.request.user)
        obj.previous_post = previous_obj
        previous_obj.next_post = obj
        obj.save()
        previous_obj.save()
        return redirect(reverse('posts:detail', kwargs={"pk": obj.pk}))