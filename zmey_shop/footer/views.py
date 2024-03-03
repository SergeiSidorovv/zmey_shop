from django.views.generic.base import TemplateView


class About(TemplateView):
    """Transfers to the template page about shop"""
    template_name = "footer/about.html"
