from django.views.generic import TemplateView
# Create your views here.

class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class HomePageView(TemplateView):
    template_name = 'home.html'