#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect
#from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Article


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'latest_articles_list'

    def get_queryset(self):
        """
        Excludes any article in the future
        """
        return Article.objects.filter(
                a_pub_date__lte=timezone.now()
                ).order_by('-a_pub_date')[:25]


class DetailView(generic.DetailView):
    model = Article
    template_name = 'books/detail.html'

    def get_queryset(self):
        """
        Excludes any article in the future
        """
        return Article.objects.filter(
                a_pub_date__lte=timezone.now()
                )
