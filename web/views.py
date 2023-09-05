from django.views.generic import TemplateView,ListView
from django.shortcuts import render,redirect
from .models import Portfolio,Knowledge
from .forms import ContactForm



class IndexView(TemplateView):
    template_name = "web/index.html"
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "is_index": True,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact-me')
        
        context = {
            "is_index": True,
            "form": form,
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    model = Knowledge
    template_name = "web/about.html"
    knowledge = 'knowledge'
    knwlge = Knowledge.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_about"] = True
        return context

class ResumeView(TemplateView):
    template_name = "web/resume.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_resume"] = True
        return context
    
    

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'web/portfolio.html'
    context_object_name = 'portfolio'
    queryset = Portfolio.objects.all()  # Optionally, you can define a custom queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_portfolio"] = True
        return context



class ContactView(TemplateView):
    template_name = 'web/contact.html'  # Specify the template name

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "is_contact": True,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact-me')
        
        context = {
            "is_contact": True,
            "form": form,
        }
        return render(request, self.template_name, context)
