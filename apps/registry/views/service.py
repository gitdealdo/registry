from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.utils.text import capfirst
from django.utils.encoding import force_bytes, force_text

from apps.utils.util import empty

from ..models.service import Service
from ..forms.service import ServiceModelForm


class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'service/list.html'

    def get_paginate_by(self, queryset):
        if 'all' in self.request.GET:
            return None
        return ListView.get_paginate_by(self, queryset)

    def get_queryset(self):
        self.paginate_by = empty(self.request, 'paginate_by', 10)
        self.o = empty(self.request, 'o', 'code')
        self.f = empty(self.request, 'f', 'description')
        self.q = empty(self.request, 'q', '')
        column_contains = u'%s__%s' % (self.f, 'contains')
        query = {column_contains: self.q}
        return self.model.objects.filter(**query).order_by(self.o)

    def get_context_data(self, **kwargs):
        context = super(ServiceList, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['title'] = "Seleccione servicio para modificar"
        return context


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'service/form.html'
    success_url = reverse_lazy('registry:service_list')

    def get_context_data(self, **kwargs):
        context = super(ServiceCreateView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['title'] = "Registrar nuevo Servicio"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=True)
        msg = (' %(name)s "%(obj)s" fue creado satisfactoriamente.') % {
            'name': capfirst(force_text(self.model._meta.verbose_name)),
            'obj': force_text(self.object)
        }
        if self.object.id:
            messages.success(self.request, msg)
        return super(ServiceCreateView, self).form_valid(form)


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'service/form.html'
    success_url = reverse_lazy('registry:service_list')

    def get_context_data(self, **kwargs):
        context = super(ServiceUpdateView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['title'] = 'Actualizar servicio'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=True)
        msg = '%(name)s "%(obj)s" fue cambiado satisfactoriamente.' % {
            'name': capfirst(force_text(self.model._meta.verbose_name)),
            'obj': force_text(self.object)
        }
        messages.success(self.request, msg)
        return super(ServiceUpdateView, self).form_valid(form)
    

class ServiceDeleteView(View):
    success_url = reverse_lazy('registry:service_list' )

    def get(self, request, pk, *args, **kwargs):
        Service.objects.get(id=pk).delete()
        messages.success(request, "Servicio eliminado correctamente")
        return HttpResponseRedirect(self.success_url)


# class ServiceDeleteView(LoginRequiredMixin, DeleteView):
#     model = Service
#     success_url = reverse_lazy('registry:service_list' )
#     template_name = 'service/confirm_delete.html'

#     def get_context_data(self, **kwargs):
#         context = super(ServiceDeleteView, self).get_context_data(**kwargs)
#         context['opts'] = self.model._meta
#         context['title'] = ('Eliminar categoría %s') % self.object
#         return context

#     def delete(self, request, *args, **kwargs):
#         try:
#             d = self.get_object()
#             d.delete()
#             msg = (' %(name)s "%(obj)s" fue eliminado satisfactorialmente.') % {
#                 'name': capfirst(force_text(self.model._meta.verbose_name)),
#                 'obj': force_text(d)
#             }
#             if not d.id:
#                 messages.success(self.request, msg)
#         except Exception as e:
#             messages.error(request, e)
#         return HttpResponseRedirect(self.success_url)

