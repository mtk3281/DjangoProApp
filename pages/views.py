from django.views.generic import TemplateView
from blogs.models import BlogPost

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bgimage'] = 'assets/img/home-bg.jpg'
        context['posts'] = BlogPost.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bgimage'] = 'assets/img/about-bg.jpg'
        return context


class ContactPageView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bgimage'] = 'assets/img/contact-bg.jpg'
        return context
