from django.urls import reverse
from django.views import generic

from .models import Article

class IndexView(generic.ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'article_list'

class DetailView(generic.DetailView):
    model = Article
    template_name = 'articles/detail.html'

class CreateView(generic.edit.CreateView):
    model = Article
    fields = ['title','author','body_text']

    def get_success_url(self) -> str:
        return reverse('articles:index')