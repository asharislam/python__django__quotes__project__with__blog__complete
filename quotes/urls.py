from quotes.views import HomeView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    path('home/', views.HomeView.as_view(), name='home'),
    path('index/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contract/', views.ContractView.as_view(), name='contract'),
    path('quote/', views.QuoteView.as_view(), name='quote'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    

]
