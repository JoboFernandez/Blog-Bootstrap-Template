from django.views.generic.edit import UpdateView
from django.shortcuts import redirect, reverse

from ..models import Post, Author


class PostUpdateView(UpdateView):
    template_name = 'posts/post_form.html'
    model = Post
    fields = ['title', 'thumbnail', 'categories', 'featured', 'overview', 'content', 'previous_post', 'next_post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.filter(featured=True)[:3]
        context['action'] = 'Update'
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = Author.objects.get(user=self.request.user)
        obj.save()
        return redirect(reverse('posts:detail', kwargs={"pk": obj.pk}))