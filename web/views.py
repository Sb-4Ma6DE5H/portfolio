from django.views.generic import TemplateView


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
    

class PortfolioView(TemplateView):
    template_name = "web/portfolio.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_portfolio"] = True
        return context
    
class ContactView(TemplateView):
    template_name = "web/contact.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_contact"] = True
        return context