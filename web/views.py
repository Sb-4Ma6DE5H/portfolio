from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from .models import Portfolio
from .forms import ContactForm



class IndexView(TemplateView):
    template_name = "web/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_index"] = True
        return context

class AboutView(TemplateView):
    template_name = "web/about.html"
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
    

# class PortfolioView(TemplateView):
#     template_name = "web/portfolio.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["is_portfolio"] = True
#         context["portfolio_items"] = Portfolio.objects.all()  # Fetch all portfolio items
#         return context
    
def portfolio_view(request):
    portfolio = Portfolio.objects.all()
    context = {
        "is_portfolio": True,
        "portfolio": portfolio,
    }
    return render(request, "web/portfolio.html", context)
    
# class ContactView(TemplateView):
#     template_name = "web/contact.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["is_contact"] = True
#         return context



def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            
            return redirect('/contact-me')
        else:
           form = ContactForm()
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
        return render(request, "web/contact.html", context)