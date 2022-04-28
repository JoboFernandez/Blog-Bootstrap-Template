from django.shortcuts import redirect, reverse
from django.views.generic import ListView

from ..models import Post
from subscriptions.forms import SubscriptionForm


class IndexListView(ListView):
    template_name = 'index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-timestamp_created')[:3]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SubscriptionForm
        context['featured_posts'] = Post.objects.filter(featured=True).order_by('-timestamp_created')[:3]
        return context

    def post(self, request):
        form = SubscriptionForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(reverse('index'))
