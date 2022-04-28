from django.db.models import Count, Q
from django.views.generic import ListView

from ..models import Post


class PostListView(ListView):
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-timestamp_created')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(overview__icontains=query)
            ).distinct()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all().order_by('-timestamp_created')[:3]
        context['featured_posts'] = Post.objects.filter(featured=True)[:3]
        context['category_count'] = Post.objects.values('categories__category_name').annotate(dcount=Count('categories')).order_by()
        query = self.request.GET.get('q')
        context['query'] = '' if query is None else query
        return context
