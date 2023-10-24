from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = settings.LOGIN_REDIRECT_URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = '¡Bienvenido a la página de inicio!'
        return context
    

class MessageView(LoginRequiredMixin, TemplateView):
    template_name = 'client.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = '¡Este es un mensaje !'
        return context

