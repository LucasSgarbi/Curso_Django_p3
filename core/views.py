from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, Recurso
from .forms import ContatoForms


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForms
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        context['recursos_L'] = Recurso.objects.all()[:3]
        context['recursos_R'] = Recurso.objects.all()[3:6]
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enivar o E-mail')
        return super(IndexView, self).form_invalid(form, *args, *kwargs)