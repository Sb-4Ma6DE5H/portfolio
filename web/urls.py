from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('MyResume', views.ResumeView.as_view(), name='resume'),
    path('MyPortfolio', views.PortfolioView.as_view(), name='portfolio'),
    path('contact-me', views.ContactView.as_view(), name='contact'),
]