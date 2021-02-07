from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic.edit import DeleteView, UpdateView
from .models import Article
from .forms import ArticleModelForm
from django.views.generic import (
  ListView,
  DetailView,
  CreateView
)

class ArticleCreateView(CreateView):
  template_name = 'articles/article_create.html'
  form_class = ArticleModelForm
  queryset = Article.objects.all()
  success_url = '../'

class ArticleUpdateView(UpdateView):
  template_name = 'articles/article_create.html'
  form_class = ArticleModelForm
  queryset = Article.objects.all()
  success_url = '../'

class ArticleListView(ListView):
  template_name = 'articles/article_list.html'
  queryset = Article.objects.all()

class ArticleDetailView(DetailView):
  template_name = 'articles/article_detail.html'
  queryset = Article.objects.all()
  
  # def get_object(self):
  #   id_ = self.kwargs.get("id")
  #   return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
  template_name = 'articles/article_delete.html'
  queryset = Article.objects.all()

  def get_success_url(self):
      return reverse('articles:article-list')