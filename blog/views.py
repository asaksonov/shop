from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from pytils.translit import slugify

from .models import Article


class ArticleListView(ListView):
    model = Article

    extra_context = {
        'title': 'SkyStore | Блог',
        'nbar': 'blog'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleCreateView(CreateView):
    model = Article

    fields = (
        'title',
        'slug',
        'content',
        'preview',
        'is_published'
    )

    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article

    fields = (
        'title',
        'slug',
        'content',
        'preview',
        'is_published'
    )

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        article_pk = self.kwargs.get('pk')
        context_data['title'] = self.model.objects.get(pk=article_pk).title
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
