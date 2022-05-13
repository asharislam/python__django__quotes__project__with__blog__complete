from quotes import models
from django.db.models import query
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

from . models import QuoteCategory
from . models import Quote

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContractView(TemplateView):
    template_name = "contract.html"

class QuoteView(ListView):
    template_name = "quote.html"
    model = Quote
    
    def get_queryset(self):
        query_set =super().get_queryset()
        return query_set.select_related
        ('quote_category')


class BlogView(TemplateView):
    template_name = "blog.html"
