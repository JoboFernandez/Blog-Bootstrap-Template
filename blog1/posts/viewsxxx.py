from django.db.models import Count, Q
from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView

from .models import Post, PostView
from .forms import CommentForm
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


class BlogListView(ListView):
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 2

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


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    context_object_name = 'post'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all().order_by('-timestamp_created')[:3]
        context['featured_posts'] = Post.objects.filter(featured=True)[:3]
        context['category_count'] = Post.objects.values('categories__category_name').annotate(dcount=Count('categories')).order_by()
        query = self.request.GET.get('q')
        context['query'] = '' if query is None else query
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        context['comments'] = self.object.comments.all()
        PostView.objects.get_or_create(user=self.request.user, post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST or None)
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        # context['comments'] = self.object.comment.all()
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.post = Post.objects.get(id=self.object.pk)
            comment_form.save()
        return self.render_to_response(context=context)

